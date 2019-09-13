import socketserver
from time import ctime

"""http://collabedit.com/ssfen"""


class CustomRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        data = ctime().encode()

        socket.sendto(data.upper(), self.client_address)


def main():
    server_address = 'localhost', 8989
    server = socketserver.UDPServer(server_address, CustomRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
