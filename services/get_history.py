import sqlite3


def get_history(user_id):

    conn = sqlite3.connect("reconhub.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            target,
            target_type,
            risk_score,
            risk_level,
            scan_time
        FROM scans
        WHERE user_id = ?
        ORDER BY id DESC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows