import socketserver
from time import ctime


class CustomRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('recv : ', self.client_address)
        ts = ctime().encode()   # convert into bytes
        self.request.sendall(ts)

def main():
    server_address = 'localhost', 8989
    server = socketserver.TCPServer(server_address, CustomRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
