import requests
from services.cpe_lookup import get_cpe


TECH_MAPPING = {
    "WordPress": "wordpress",
    "Apache": "apache http server",
    "Nginx": "nginx",
    "jQuery": "jquery",
    "Bootstrap": "bootstrap",
    "PHP": "php",
    "React": "react.js",
    "Vue.js": "vue.js",
    "Angular": "angular",
    "Next.js": "next.js",
    "Drupal": "drupal",
    "Joomla": "joomla",
    "Express.js": "express",
    "ASP.NET": "asp.net"
}


def get_cves(technologies):

    cves = []
    seen = set()

    for category, tech in technologies:

        keyword = TECH_MAPPING.get(tech, tech)

        # Try to get official CPE
        cpe = get_cpe(keyword)

        try:

            if cpe:
                url = (
                    "https://services.nvd.nist.gov/rest/json/cves/2.0"
                    f"?cpeName={cpe}"
                )
            else:
                url = (
                    "https://services.nvd.nist.gov/rest/json/cves/2.0"
                    f"?keywordSearch={keyword}"
                )

            response = requests.get(url, timeout=20)
            data = response.json()

            if "vulnerabilities" not in data:
                continue

            for item in data["vulnerabilities"][:3]:

                cve = item["cve"]
                cve_id = cve["id"]

                if cve_id in seen:
                    continue

                seen.add(cve_id)

                description = ""

                for desc in cve.get("descriptions", []):

                    if desc.get("lang") == "en":
                        description = desc.get("value", "")
                        break

                cves.append({
                    "technology": tech,
                    "id": cve_id,
                    "description": description[:120] + ("..." if len(description) > 120 else "")
                })

        except Exception as e:
            print(f"CVE Lookup Error ({tech}): {e}")

    return cves