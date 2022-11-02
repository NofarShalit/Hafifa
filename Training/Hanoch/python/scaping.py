from scapy.all import *


def main():
    
    # Send data through ICMP- ICMP tunnel
    p = sr1(IP(dst="1.1.1.1")/ICMP()/"data")
    
    # Sniff HTTP packets
    pcap = sniff(filter='icmp', count=100)
    pcap.summary()
    wrpcap("mycap.pcap", pcap)


    
if __name__ == '__main__':
    main()