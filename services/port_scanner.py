import socket


COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}


def scan_ports(host):

    open_ports = []

    for port, service in COMMON_PORTS.items():

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((host, port))

            if result == 0:
                open_ports.append({
                    "port": port,
                    "service": service
                })

            sock.close()

        except:
            pass

    return open_ports