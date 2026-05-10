import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT
)
''')

conn.commit()


def save_memory(text):
    cursor.execute(
        "INSERT INTO memories(content) VALUES(?)",
        (text,)
    )
    conn.commit()


def get_memories():
    cursor.execute("SELECT content FROM memories")
    return [row[0] for row in cursor.fetchall()]
