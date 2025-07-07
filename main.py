import streamlit as st
from dotenv import load_dotenv
import os

from gmail_utils import authenticate_gmail, get_recent_emails
from memory import init_memory, get_pending_tasks
from langgraph.graph import StateGraph, END
from nodes.classify import node_classify
from nodes.act import node_act
from typing import TypedDict
load_dotenv()
init_memory()

class EmailState(TypedDict):
    sender: str
    subject: str
    body: str

# Build LangGraph flow
workflow = StateGraph(EmailState)
workflow.add_node("classify", node_classify)
workflow.add_node("act", node_act)
workflow.set_entry_point("classify")
workflow.add_edge("classify", "act")
workflow.add_edge("act", END)
graph = workflow.compile()

# Streamlit UI
st.set_page_config(page_title="A-E³ Bot", layout="wide")
st.title("📧 A-E³: Autonomous Email Execution Engine")

if "gmail_service" not in st.session_state:
    with st.spinner("Authenticating Gmail..."):
        st.session_state.gmail_service = authenticate_gmail()

if st.button("📥 Process Latest Emails"):
    emails = get_recent_emails(st.session_state.gmail_service)

    for email in emails:
        with st.expander(f"From: {email['sender']} | Subject: {email['subject']}"):
            st.text_area("Email Body", value=email['body'], height=150)
            result = graph.invoke(email)
            st.success(f"✅ Action Taken: {result.get('status')}")
            if result.get("reply"):
                st.markdown(f"**Draft Reply:** {result['reply']}")
            if result.get("reminder"):
                st.markdown(f"⏰ Reminder Set: {result['reminder']}")

if st.button("📋 Show Pending Tasks"):
    tasks = get_pending_tasks()
    if tasks:
        st.subheader("🗂️ Tasks in Memory")
        for t in tasks:
            st.markdown(f"- **{t[1]}** → _{t[2]}_ by **{t[3]}**")
    else:
        st.info("No tasks stored yet.")
