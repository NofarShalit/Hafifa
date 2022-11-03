from scapy.all import *

def main():
    # Sending data over ICMP packets
    Datagram = send(IP(dst='10.0.0.4')/ICMP()/"dataddddddddddddddddddddddddddddddddddddddddddddd")

if __name__ == "__main__":
    main()