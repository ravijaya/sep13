"""demo for the bytes"""

s = 'peter pan'
print(s)
print(type(s))
print()

s = b'peter pan'
print(s)
print(type(s))
print()

print(s.decode())  # bytes into unicode/str
print()

s = 'peter pan'
print(s.encode())   # unicode to bytes