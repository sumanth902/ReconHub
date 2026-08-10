def get_google_dorks(domain):

    return [

        f"site:{domain}",

        f"site:{domain} login",

        f"site:{domain} admin",

        f"site:{domain} inurl:admin",

        f"site:{domain} inurl:login",

        f"site:{domain} intitle:index.of",

        f"site:{domain} filetype:pdf",

        f"site:{domain} filetype:doc",

        f"site:{domain} ext:sql",

        f"site:{domain} ext:bak",

        f"site:{domain} ext:env",

        f"site:{domain} ext:log",

        f"site:{domain} \"password\"",

        f"site:{domain} \"confidential\"",

        f"site:{domain} \"api\""
    ]