import socket

from SocketServer import TCPServer, StreamRequestHandler

class EchoRequestServer(StreamRequestHandler):
    
    def handle(self):
        while True:
            try:
                line = self.rfile.readline()
            except socket.error:
                break
            if not line or line.find("exit") == 0:
                break
            
            self.wfile.write("You wrote: " + line)
                
if __name__ == "__main__":
    server = TCPServer(('', 8001), EchoRequestServer)
    server.serve_forever()