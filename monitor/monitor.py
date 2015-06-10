import os,sys
import SimpleHTTPServer
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
httpPort = 8080

class SecurityMonitorRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        rootdir = ''
        try:
            if self.path.endswith('.html'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header('Content-type','text-html')
                self.end_headers()
                
                self.write.write(f.read())
                f.close()
                return
        except IOError:
            self.send_error(404,'Datei nicht gefunden')

def run():
    print ("Starte HTTP-Dienst neu")
    server_address = ('127.0.0.1', 8080)
    httpDaemon = HTTPServer(server_address, SecurityMonitorRequestHandler)
    print ('HTTP-Dienst laeuft')
    httpDaemon.serve_forever()
if __name__ == '__main__':
    run()
