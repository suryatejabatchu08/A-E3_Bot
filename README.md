# A-E³ Bot: Autonomous Email Execution Engine

A-E³ Bot is an intelligent assistant that automates your email workflow. It classifies incoming emails, determines the necessary actions, extracts tasks and deadlines, and helps you stay on top of your commitments with reminders – all from your Gmail account, using modern LLMs.

---

## Features

- **Gmail Integration**: Securely connects to your Gmail to fetch recent emails.
- **LLM-powered Email Classification**: Uses generative AI to analyze and classify emails by intent (task, meeting, newsletter, spam, update).
- **Action Extraction**: Automatically detects if action is required and summarizes next steps.
- **Deadline Recognition**: Extracts deadlines from email text (e.g., "Thursday", "Friday") and sets reminders accordingly.
- **Task Memory**: Stores tasks and their deadlines in a persistent local database.
- **Auto-Reply Drafts**: Suggests reply content for actionable emails.
- **Reminders**: Sets up reminders based on extracted deadlines.
- **Interactive UI**: Streamlit-based user interface for easy operation and visualization.

---

## How It Works

1. **Authentication**: User authenticates with Gmail via OAuth2.
2. **Email Retrieval**: Recent emails are fetched using the Gmail API.
3. **Classification**: Each email is analyzed by an LLM (Google Gemini) to detect intent, required actions, and to summarize.
4. **Action Handling**: If action is required, a task is stored, a deadline is extracted, and a draft reply/reminder is generated.
5. **UI Interaction**: Users can view processed emails, take suggested actions, and manage pending tasks from the Streamlit dashboard.

---

## Project Structure

```
.
├── main.py                 # Streamlit app and workflow orchestration
├── nodes/
│   ├── classify.py         # Email classification node (LLM-powered)
│   └── act.py              # Action node: stores tasks, drafts replies, sets reminders
├── memory.py               # Persistent task storage (SQLite)
├── gmail_utils.py          # Utilities for Gmail authentication and email fetching
├── requirements.txt        # Python dependencies
└── .env.example            # Example environment variables
```

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/suryatejabatchu08/A-E3_Bot.git
cd A-E3_Bot
```

### 2. Install Python dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set up Environment Variables

- Copy `.env.example` to `.env` and fill in your values:

```
GEMINI_API_KEY=your_google_gemini_api_key
GOOGLE_CLIENT_SECRET_FILE=path_to_your_gmail_client_secret.json
```

- [Obtain a Google Gemini API key](https://ai.google.dev/gemini-api/docs/api-key).
- [Create Gmail API credentials](https://console.cloud.google.com/apis/credentials).

### 4. Run the App

```bash
streamlit run main.py
```

---

## Usage

- **Process Emails**: Click "Process Latest Emails" to fetch, classify, and act on incoming emails.
- **View Tasks**: Click "Show Pending Tasks" to list tasks with deadlines.
- **Review Replies/Reminders**: Each actionable email will display a suggested reply and reminder.

---

## Customization

- **LLM Model**: The default is Google Gemini (`gemini-2.0-flash`). You can change this in `nodes/classify.py`.
- **Deadline Parsing**: The logic for extracting deadlines is in `nodes/act.py`. You can extend it for more advanced date detection.
- **Database**: By default, tasks are stored in `memory.db` (SQLite). You can adapt `memory.py` for other backends.

---

## Contributing

1. Fork the repo.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Open a Pull Request.

