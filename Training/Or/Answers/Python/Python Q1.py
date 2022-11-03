from scapy.all import *

capture = sniff(iface="Ethernet",  filter="port 53", count=5, prn=lambda x:x.summary())
capture.summary()