import requests


def get_robots(domain):
    """
    Fetch robots.txt from the target website.
    """

    try:
        url = f"https://{domain}/robots.txt"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return {
                "status": "Found",
                "content": response.text
            }

        return {
            "status": "Not Found",
            "content": ""
        }

    except Exception as e:
        return {
            "status": "Error",
            "content": str(e)
        }