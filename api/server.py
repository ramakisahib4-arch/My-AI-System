from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class AIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            response = {
                "status": "online",
                "service": "My AI System API"
            }

            self.send_response(200)
            self.send_header(
                "Content-type",
                "application/json"
            )
            self.end_headers()

            self.wfile.write(
                json.dumps(response).encode()
            )

        else:
            self.send_response(404)
            self.end_headers()


def start_server():
    server = HTTPServer(
        ("0.0.0.0", 8080),
        AIHandler
    )

    print("AI API running on port 8080")
    server.serve_forever()


if __name__ == "__main__":
    start_server()
