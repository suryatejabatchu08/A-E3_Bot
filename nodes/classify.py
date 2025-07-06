from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(api_key=os.getenv("GEMINI_API_KEY"), model="gemini-pro")

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
    return eval(response)

def node_classify(state):
    result = classify_email.invoke(state['body'])
    return {**state, **result}
