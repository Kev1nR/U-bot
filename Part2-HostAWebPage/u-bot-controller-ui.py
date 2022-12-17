# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import ViaHBridge
import json
from urllib.parse import urlparse, parse_qs


hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def bridge (self):
        path = '/index.html'
        try:
            #Reading the file
            file_to_open = open(path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
    
    def do_GET(self):
        
        if self.path == '/':
            self.path = '/index.html'
        try:
            #Reading the file
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
    
    def do_POST(self):
        #URL='https://someurl.com/with/query_string?i=main&mode=front&sid=12ab&enc=+Hello'
        parsed_url = urlparse(self.path)
        qs = parse_qs(parsed_url.query)
        print (qs)
        #body = self.rfile.read(int(self.headers['Content-Length']))
        print (self.path)
        #command = json.loads(body)
        dirn = qs["dirn"][0]
        speed = float(qs["speed"][0])
        
        if (dirn == "Stop"):
            ViaHBridge.allStop()
        if (dirn == "Forward"):
            ViaHBridge.forwardDrive(speed)
        if (dirn == "Reverse"):
            ViaHBridge.reverseDrive(speed)
        if (dirn == "Left"):
            ViaHBridge.spinAntiClockwise(speed)
        if (dirn == "Right"):
            ViaHBridge.spinClockwise(speed)
        
        bridge(self)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")