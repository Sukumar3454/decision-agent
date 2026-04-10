import sqlite3
import json

def init_db():
    conn = sqlite3.connect("decision.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input_data TEXT,
        decision TEXT,
        reasoning TEXT,
        llm_explanation TEXT,
        latency REAL,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_to_db(input_data, result, latency, timestamp):
    conn = sqlite3.connect("decision.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO results (input_data, decision, reasoning, llm_explanation, latency, timestamp)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        json.dumps(input_data),
        result["decision"],
        json.dumps(result["reasoning"]),
        result.get("llm_explanation", ""),
        latency,
        timestamp
    ))

    conn.commit()
    conn.close()