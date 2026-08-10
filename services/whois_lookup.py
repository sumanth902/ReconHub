import whois
from datetime import datetime


def format_date(date_value):
    """
    Convert WHOIS date to a readable format.
    """

    if isinstance(date_value, list):
        date_value = date_value[0]

    if isinstance(date_value, datetime):
        return date_value.strftime("%Y-%m-%d")

    return str(date_value)


def get_whois(domain):
    try:
        w = whois.whois(domain)

        return {
            "domain": w.domain_name,
            "registrar": w.registrar,
            "creation_date": format_date(w.creation_date),
            "expiration_date": format_date(w.expiration_date),
            "name_servers": sorted(list(w.name_servers)) if w.name_servers else [],
            "emails": w.emails
        }

    except Exception as e:
        return {
            "error": str(e)
        }