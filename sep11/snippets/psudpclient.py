import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    server_address = ('localhost', 8989)
    sock.sendto(bytes('' + "\n", "utf-8"), server_address)
    payload = str(sock.recv(1024), "utf-8")

    print(payload)
except (ConnectionRefusedError, OSError) as err:
    print('unavailable service @ {}:{}'.format(*server_address))
finally:
    sock.close()
