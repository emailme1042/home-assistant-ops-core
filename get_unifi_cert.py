#!/usr/bin/env python3
import ssl
import socket

# Get certificate from UniFi controller
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

try:
    with socket.create_connection(("192.168.0.1", 443)) as sock:
        with context.wrap_socket(sock, server_hostname="192.168.0.1") as ssock:
            cert = ssock.getpeercert(binary_form=True)

    # Write to file
    with open("unifi_cert.pem", "w") as f:
        f.write(ssl.DER_cert_to_PEM_cert(cert))

    print("Certificate saved to unifi_cert.pem")
except Exception as e:
    print(f"Error: {e}")