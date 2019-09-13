"""find & replacment """
import re

s = 'nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin'
pattern = ':'
replacement = ','

s2 = re.sub(pattern, replacement, s)
print(s2)
print()

s2 = re.sub(pattern, replacement, s, count=1)
print(s2)
print()
