import json
import os


def export_json(results):
    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{results['target']}_report.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    return filename