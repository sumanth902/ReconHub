import ssl
import socket
from datetime import datetime


def get_ssl_info(domain):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        return {
            "subject": dict(x[0] for x in cert["subject"]),
            "issuer": dict(x[0] for x in cert["issuer"]),
            "version": cert.get("version"),
            "serial_number": cert.get("serialNumber"),
            "valid_from": cert.get("notBefore"),
            "valid_until": cert.get("notAfter")
        }

    except Exception as e:
        return {"error": str(e)}