import sqlite3

def init_memory():
    conn = sqlite3.connect('memory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, sender TEXT, task TEXT, deadline TEXT)''')
    conn.commit()
    conn.close()

def store_task(sender, task, deadline):
    conn = sqlite3.connect('memory.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (sender, task, deadline) VALUES (?, ?, ?)", (sender, task, deadline))
    conn.commit()
    conn.close()

def get_pending_tasks():
    conn = sqlite3.connect('memory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks
