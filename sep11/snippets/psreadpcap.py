#!/usr/bin/python
from scapy.utils import PcapReader
from pprint import pprint

pkts = PcapReader("/root/ftp.pcap")  # should be in wireshark-tcpdump format

for pkt in pkts:
    pprint(pkt.show())