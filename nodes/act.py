from memory import store_task

def act_on_email(data):
    intent = data.get('intent')
    sender = data.get('sender', '')
    body = data.get('body', '')
    summary = data.get('summary', '')
    action_required = data.get('action_required', False)

    if not intent:
        return {"status": "error", "error": "No intent detected."}

    if action_required:
        # Dynamically generate task and deadline based on summary/intent
        task = summary if summary else "Follow up on email"
        # Example: extract a deadline from summary or fallback
        deadline = "Friday" if "Friday" in body else "this week"
        store_task(sender, task, deadline)
        reply = f"Hi, I’ll take action: {task}. Expected by {deadline}."
        reminder = f"{deadline} 5PM"
        status = f"Action taken for intent '{intent}': {task}"
        return {
            "reply": reply,
            "reminder": reminder,
            "status": status
        }
    else:
        status = f"No action required for intent '{intent}'"
        return {"status": status}

def node_act(state):
    print("Act node input:", state)
    result = act_on_email(state)
    print("Act node result:", result)
    return {**state, **result}