import sqlite3


def save_scan(results, user_id):

    conn = sqlite3.connect("reconhub.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO scans
        (
            target,
            target_type,
            risk_score,
            risk_level,
            pdf_report,
            json_report,
            user_id
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            results["target"],
            results["target_type"],
            results["risk"]["score"],
            results["risk"]["level"],
            results.get("pdf_report", ""),
            results.get("json_report", ""),
            user_id
        )
    )

    conn.commit()
    conn.close()