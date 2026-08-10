import sqlite3


def get_history():

    conn = sqlite3.connect("reconhub.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            target,
            target_type,
            risk_score,
            risk_level,
            scan_time
        FROM scans
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows