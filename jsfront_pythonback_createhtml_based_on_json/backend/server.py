import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Data to serve
data = [
    {
        "name": "Mr. Feller",
        "age": 11,
        "good_in": ["typer", "math", "programming", "scratch", "swimming", "js"]
    },
    {
        "name": "Tony",
        "age": 7,
        "good_in": ["mobile", "speak", "run"]
    },
    {
        "name": "Zico",
        "age": 0,
        "good_in": ["bark", "run", "mess"]
    },
    {
        "name":"Zica",
        "age":"Dead",
        "good_in":["to be a ghost"]
    }
]

class SimpleJSONHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set response status code and headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Write JSON data
        self.wfile.write(json.dumps(data).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleJSONHandler, port=8002):
    server_address = ('0.0.0.0', port)  # Listen on all network interfaces
    httpd = server_class(server_address, handler_class)
    print(f'Serving JSON on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

