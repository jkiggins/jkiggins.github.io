#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def serve():
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving at: http://localhost:{PORT}")
            print(f"Open: http://localhost:{PORT}/next.html to preview")
            print("Press Ctrl+C to stop.")
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 98: # Address already in use
            print(f"Error: Port {PORT} is already in use.")
            print("Try running: lsof -i :8000 to find the process, or manually serve using:")
            print(f"python3 -m http.server <port>")
        else:
            print(f"An error occurred: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)

if __name__ == "__main__":
    serve()
