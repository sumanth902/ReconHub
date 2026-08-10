import requests


def http_fingerprint(domain):

    try:

        url = f"https://{domain}"

        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        headers = response.headers

        data = {
            "Status Code": response.status_code,
            "Server": headers.get("Server", "Unknown"),
            "X-Powered-By": headers.get("X-Powered-By", "Not Found"),
            "Content-Type": headers.get("Content-Type", "Unknown"),
            "Content-Length": headers.get("Content-Length", "Unknown"),
            "Strict-Transport-Security": headers.get("Strict-Transport-Security", "Not Found"),
            "Content-Security-Policy": headers.get("Content-Security-Policy", "Not Found"),
            "X-Frame-Options": headers.get("X-Frame-Options", "Not Found"),
            "Referrer-Policy": headers.get("Referrer-Policy", "Not Found"),
            "Permissions-Policy": headers.get("Permissions-Policy", "Not Found"),
        }

        return data

    except Exception as e:
        return {"Error": str(e)}