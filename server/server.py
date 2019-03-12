from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class SimpleHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type','text/html')
        self.end_headers()
        # Data
        message = "Hoc Lap Trinh Tai Toidicode.com"
        self.wfile.write(bytes(message, "utf8"))
        return

server_address = ('127.0.0.1', 8000)

httpd = HTTPServer(server_address, SimpleHTTP)

httpd.serve_forever()
