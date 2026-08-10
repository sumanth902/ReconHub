import re
import ipaddress

def detect_target(target):

    target = target.strip()

    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if re.match(email_pattern, target):
        return "email"

    try:
        ipaddress.ip_address(target)
        return "ip"
    except ValueError:
        pass

    domain_pattern = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'

    if re.match(domain_pattern, target):
        return "domain"

    return "username"