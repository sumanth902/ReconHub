def get_modules(target_type):

    modules = {

        "domain": [
            "WHOIS",
            "DNS",
            "Subdomains",
            "Wappalyzer",
            "Wayback",
            "Archive.today",
            "Google Dorks",
            "Security Headers",
            "Open Ports"
        ],

        "ip": [
            "Reverse DNS",
            "IP WHOIS",
            "Open Ports"
        ],

        "email": [
            "Email Validation",
            "MX Lookup"
        ],

        "username": [
            "Sherlock"
        ]

    }

    return modules.get(target_type, [])