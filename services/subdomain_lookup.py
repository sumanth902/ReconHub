import requests


def get_subdomains(domain):

    subdomains = set()

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # -------- AlienVault --------

    try:

        url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"

        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code == 200:

            data = response.json()

            for item in data.get("passive_dns", []):

                host = item.get("hostname")

                if host:
                    subdomains.add(host)

    except Exception:
        pass

    # -------- HackerTarget --------

    try:

        url = f"https://api.hackertarget.com/hostsearch/?q={domain}"

        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code == 200:

            for line in response.text.splitlines():

                host = line.split(",")[0]

                if host.endswith(domain):
                    subdomains.add(host)

    except Exception:
        pass

    return sorted(subdomains)