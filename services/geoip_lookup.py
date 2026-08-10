import requests
import socket


def get_geoip(domain):

    try:

        ip = socket.gethostbyname(domain)

        url = f"http://ip-api.com/json/{ip}"

        response = requests.get(url, timeout=10)

        data = response.json()

        return {

            "ip": ip,
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "isp": data.get("isp"),
            "org": data.get("org"),
            "asn": data.get("as"),
            "timezone": data.get("timezone"),
            "lat": data.get("lat"),
            "lon": data.get("lon")

        }

    except Exception as e:

        return {
            "error": str(e)
        }
    