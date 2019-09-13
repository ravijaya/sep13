from pprint import pprint as pp
import psutil

"""https://pastebin.com/raw/gurgefC4"""
for nic, list_of_addresses in psutil.net_if_addrs().items():
    print(nic)

    for address in list_of_addresses:
        print(address.family)
        print(address.address)
        print(address.netmask)
        print(address.broadcast)
        print()
    print()