import dns.resolver


def email_security(domain):

    result = {
        "SPF": "Not Found",
        "DKIM": "Not Found",
        "DMARC": "Not Found"
    }

    # SPF
    try:
        answers = dns.resolver.resolve(domain, "TXT")

        for record in answers:
            text = "".join(record.strings[0].decode() if isinstance(record.strings[0], bytes) else record.strings[0])

            if text.startswith("v=spf1"):
                result["SPF"] = text

    except:
        pass

    # DMARC
    try:
        answers = dns.resolver.resolve(f"_dmarc.{domain}", "TXT")

        for record in answers:
            text = "".join(record.strings[0].decode() if isinstance(record.strings[0], bytes) else record.strings[0])

            if text.startswith("v=DMARC1"):
                result["DMARC"] = text

    except:
        pass

    # DKIM (Google selector)

    selectors = [
        "google",
        "default",
        "selector1",
        "selector2"
    ]

    for selector in selectors:

        try:

            answers = dns.resolver.resolve(
                f"{selector}._domainkey.{domain}",
                "TXT"
            )

            for record in answers:

                text = "".join(record.strings[0].decode() if isinstance(record.strings[0], bytes) else record.strings[0])

                if "k=rsa" in text:

                    result["DKIM"] = f"Found ({selector})"

                    return result

        except:
            pass

    return result