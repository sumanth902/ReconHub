import requests


def get_security_headers(domain):
    """
    Fetch HTTP security headers from a website.
    """

    try:
        url = f"https://{domain}"

        response = requests.get(url, timeout=10)

        headers = response.headers

        return {
            "Strict-Transport-Security": headers.get("Strict-Transport-Security", "Not Found"),
            "Content-Security-Policy": headers.get("Content-Security-Policy", "Not Found"),
            "X-Frame-Options": headers.get("X-Frame-Options", "Not Found"),
            "X-Content-Type-Options": headers.get("X-Content-Type-Options", "Not Found"),
            "Referrer-Policy": headers.get("Referrer-Policy", "Not Found"),
            "Permissions-Policy": headers.get("Permissions-Policy", "Not Found")
        }

    except Exception as e:
        return {
            "error": str(e)
        }