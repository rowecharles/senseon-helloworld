from http.server import BaseHTTPRequestHandler, HTTPServer

SERVER_ADDRESS = ""
SERVER_PORT = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://techtest.senseon.io</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Welcome to Senseon.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    web_server = HTTPServer((SERVER_ADDRESS, SERVER_PORT), MyServer)
    print("Server started http://%s:%s" % (SERVER_ADDRESS, SERVER_PORT))

    web_server.serve_forever()
    web_server.server_close()
    print("Server stopped.")
