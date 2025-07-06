from memory import store_task

def act_on_email(data):
    intent = data.get('intent')
    sender = data.get('sender', '')
    body = data.get('body', '')

    if not intent:
        return {"status": "error", "error": "No intent detected."}

    if intent == "task":
        task = "Review document and send feedback"
        deadline = "Friday"  # You could dynamically extract using Gemini
        store_task(sender, task, deadline)
        return {
            "reply": f"Hi, I’ll review the document and get back to you by {deadline}.",
            "reminder": "Thursday 5PM",
            "status": "task_saved"
        }
    else:
        return {"status": "no_action"}

def node_act(state):
    return {**state, **act_on_email(state)}
