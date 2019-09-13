import socket, json, pprint
s = socket.socket()
s.connect(('httpbin.org', 80))
print(s.send(b'GET /get HTTP/1.0\r\nHost: httpbin.org\r\n\r\n'))

res = s.recv(1024)
pprint.pprint(json.loads(res.decode('ascii').split('\r\n\r\n', 1)[1]))
