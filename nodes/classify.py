from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import ast
llm = ChatGoogleGenerativeAI(api_key=os.getenv("GEMINI_API_KEY"), model="gemini-2.0-flash")

import ast
import json
import re

@tool
def classify_email(email_text: str) -> dict:
    """
    Classifies an email and returns a JSON with intent, action_required, and summary.
    """
    prompt = f"""
    Classify this email. Return JSON:
    {{
        "intent": "task/meeting/newsletter/spam/update",
        "action_required": true/false,
        "summary": "brief summary"
    }}
    Email: {email_text}
    """
    response = llm.invoke(prompt)
    print(f"LLM Response: {response}")

    # Extract content if response has 'content' attribute
    if hasattr(response, "content"):
        content = response.content
    else:
        content = response

    # Remove code block markers if present
    content = re.sub(r"^```json|^```|```$", "", content, flags=re.MULTILINE).strip()

    # Try to parse as JSON
    try:
        return json.loads(content)
    except Exception:
        try:
            return ast.literal_eval(content)
        except Exception:
            return {"error": "Failed to parse response"}

def node_classify(state):
    print("Classify node input:", state)
    result = classify_email(state['body'])
    print("Classify node result:", result)
    status = f"{result.get('intent', 'Unknown')} | Action Required: {result.get('action_required', 'Unknown')}"
    return {**state, **result, "status": status}
