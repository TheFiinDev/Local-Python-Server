import http.server
import socket
import socketserver
import sys
from functools import partial

# Configuration:
PORT = 8000
BIND_ADDRESS = "0.0.0.0"
DIRECTORY = "."


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler with CORS support."""

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "Unknown"

def start_server():
    handler = partial(CustomHandler, directory=DIRECTORY)

    socketserver.ThreadingTCPServer.allow_reuse_address = True

    local_ip = get_local_ip()

    try:
        with socketserver.ThreadingTCPServer((BIND_ADDRESS, PORT), handler) as httpd:
            print("==================================================")
            print("Local development server started successfully!")
            print(f"Directory: {DIRECTORY}")
            print(f"Address (Local): http://localhost:{PORT}")
            print(f"Address (Network): http://{local_ip}:{PORT}")
            print("Stop with:  CTRL + C")
            print("==================================================")

            httpd.serve_forever()

    except PermissionError:
        print(
            f"Error: Port {PORT} requires administrator privileges.",
            file=sys.stderr,
        )
    except OSError as e:
        print(
            f"Error: {e}", 
            file=sys.stderr
        )
    except KeyboardInterrupt:
        print("\n Server stopped by user. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    start_server()