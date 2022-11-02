from scapy.all import *


def main():
    
    # Sniff HTTP packets
    pcap = sniff(filter='icmp', count=100)
    pcap.summary()
    wrpcap("mycap.pcap", pcap)

    
if __name__ == '__main__':
    main()