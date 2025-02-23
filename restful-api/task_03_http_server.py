#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data, indent=4).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            error_message = {"error": "Not Found", "message":
                             "The requested endpoint does not exist."}
            self.wfile.write(json.dumps(error_message, indent=4)
                             .encode("utf-8"))


PORT = 8000
server_adress = ("", PORT)

httpd = HTTPServer(server_adress, Handler)
print(f"Server running on http://localhost:{PORT}")
httpd.serve_forever()
