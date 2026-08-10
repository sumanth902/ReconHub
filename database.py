import sqlite3


def init_db():

    conn = sqlite3.connect("reconhub.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target TEXT,
        target_type TEXT,
        risk_score INTEGER,
        risk_level TEXT,
        scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        pdf_report TEXT,
        json_report TEXT
    )
    """)
    cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    fullname TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

    conn.commit()
    conn.close()