import requests


def get_sitemap(domain):
    """
    Fetch sitemap.xml from the target website.
    """

    urls = [
        f"https://{domain}/sitemap.xml",
        f"https://{domain}/sitemap_index.xml"
    ]

    for url in urls:
        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                return {
                    "status": "Found",
                    "url": url,
                    "content": response.text[:5000]  # First 5000 characters
                }

        except Exception:
            continue

    return {
        "status": "Not Found",
        "url": "",
        "content": ""
    }