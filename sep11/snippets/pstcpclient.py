import socket


for port in range(1):
    sock = socket.socket()
    try:
        server_address = ('localhost', 8989)
        sock.connect(server_address)
        payload = sock.recv(1024)
        print('requested :', server_address, payload.decode())  # bytes into unicode
    except (ConnectionRefusedError, OSError) as err:
        print('unavailable service @ {}:{}'.format(*server_address))
    finally:
        sock.close()
