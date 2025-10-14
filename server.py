#!/usr/bin/python3

# NOTE: Use this only for development (So that local browsers won't block the CORS requests)
import http.server
import socketserver
import argparse

# Constants
C_PURPLE = "\033[94m"
C_END = "\033[00m"

class SEDASTCPserver(socketserver.TCPServer):
    allow_reuse_address = True

parser = argparse.ArgumentParser(
    prog="SEDASDeploy",
    description="SEDAS website deployment server"
)
parser.add_argument("-p", "--port")
handler = http.server.SimpleHTTPRequestHandler

args = parser.parse_args()

try:
    print(f"{C_PURPLE}------- Running SEDASDeploy local deployment server -------{C_END}")
    with SEDASTCPserver(("", int(args.port)), handler) as httpd:
        print(f"{C_PURPLE}Local file served at http://localhost:{args.port}/index.html{C_END}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Program exited using KeyboardInterrupt (Ctrl+C)")