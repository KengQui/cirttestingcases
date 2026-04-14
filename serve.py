import http.server
import socketserver
import os

os.chdir('/home/runner/workspace')

PORT = 5000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/eval-use-cases-review.html'
        return super().do_GET()

    def log_message(self, format, *args):
        pass

socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(('0.0.0.0', PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
