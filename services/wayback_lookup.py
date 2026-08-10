import requests


def get_wayback(domain):
    try:
        url = f"https://archive.org/wayback/available?url={domain}"

        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if response.status_code != 200:
            return {
                "status": "Error",
                "error": f"HTTP {response.status_code}"
            }

        try:
            data = response.json()
        except Exception:
            return {
                "status": "Error",
                "error": "Invalid response received from Wayback API"
            }

        snapshots = data.get("archived_snapshots", {})

        if snapshots.get("closest"):

            closest = snapshots["closest"]

            return {
                "status": "Found",
                "available": closest.get("available"),
                "timestamp": closest.get("timestamp"),
                "archive_url": closest.get("url")
            }

        return {
            "status": "No Snapshot Found"
        }

    except Exception as e:
        return {
            "status": "Error",
            "error": str(e)
        }