with open("/home/ravijaya/TNSTC_.pdf", "rb") as fp:
    header = fp.read(100)


print(header[:9].decode())

