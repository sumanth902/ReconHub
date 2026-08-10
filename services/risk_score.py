def calculate_risk(results):

    score = 100

    # Missing security headers
    if "security_headers" in results:
        missing = 0

        for value in results["security_headers"].values():
            if value == "Not Found":
                missing += 1

        score -= missing * 5

    # robots.txt missing
    if results.get("robots", {}).get("status") == "Not Found":
        score -= 5

    # sitemap missing
    if results.get("sitemap", {}).get("status") == "Not Found":
        score -= 5

    # Open ports
    ports = len(results.get("ports", []))

    if ports > 5:
        score -= 15
    elif ports > 2:
        score -= 8

    # Email Security
    email = results.get("email_security", {})

    if email.get("SPF") == "Not Found":
        score -= 5

    if email.get("DKIM") == "Not Found":
        score -= 5

    if email.get("DMARC") == "Not Found":
        score -= 5

    if score < 0:
        score = 0

    if score >= 80:
        level = "Low"

    elif score >= 60:
        level = "Medium"

    else:
        level = "High"

    return {
        "score": score,
        "level": level
    }