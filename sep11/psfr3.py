

with open('/home/ravijaya/TNSTC_.pdf', 'rb') as fp:
    content = fp.read()
    print(content)
    print()

    print(content[:9].decode())