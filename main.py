from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class Recruto(BaseHTTPRequestHandler):
    def do_GET(self):
        queryParams = parse_qs(urlparse(self.path).query)
        name = queryParams.get('name', [''])[0]
        message = queryParams.get('message', [''])[0]
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response = f"<h1>Hello {name}! {message}</h1>"
        self.wfile.write(response.encode('utf-8'))

def run(server=HTTPServer, handlerClass=Recruto, port=2228):
    server_address = ('', port)
    httpd = HTTPServer(server_address, handlerClass)
    print("running on ", port)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
