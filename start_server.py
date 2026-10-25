import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

def start_server():
    port = PORT
    while port < 8100:
        try:
            httpd = ThreadedHTTPServer(("", port), CustomHandler)
            url = f"http://localhost:{port}"
            print("=" * 60, flush=True)
            print(f"ColPali Seminar Showcase Server is RUNNING at:", flush=True)
            print(f"  --> {url}", flush=True)
            print("=" * 60, flush=True)
            try:
                webbrowser.open(url)
            except Exception:
                pass
            print("Server serving forever...", flush=True)
            httpd.serve_forever()
            break
        except OSError:
            port += 1

if __name__ == "__main__":
    start_server()
