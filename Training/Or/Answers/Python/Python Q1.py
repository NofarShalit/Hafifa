from scapy.all import *

capture = sniff(iface="Ethernet",  filter="arp", count=5, prn=lambda x:x.summary())