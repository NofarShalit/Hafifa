from scapy.all import *


def main():
    
    # Send data through ICMP- ICMP tunnel
    p = send(IP(dst="10.0.0.1")/ICMP()/"command")
    
    # Sniff HTTP packets
    pcap = sniff(filter='icmp', count=100)
    pcap.summary()
    wrpcap("mycap.pcap", pcap)


    
if __name__ == '__main__':
    main()