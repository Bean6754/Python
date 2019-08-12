import http.server
import socketserver
import os

web_dir = os.path.join(os.path.dirname(__file__), 'www')
os.chdir(web_dir)

PORT = 80
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
