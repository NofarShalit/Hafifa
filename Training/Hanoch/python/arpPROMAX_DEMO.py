import subprocess as sub

from scapy.all import *


ARP_CMD = 'arp -a'
IP = 0
MAC = 1

def arp_monitor(pkt):
    if ARP in pkt and pkt[ARP].op == 2:
        print(pkt.ARP.psrc)
    
def main():
    '''
    # Detect past ARP poisonings
    proc = sub.run(ARP_CMD, shell=False,
                   capture_output=True)
    lines = proc.stdout.decode().split('\n')[3:-1]
    ##add fake arp poisoning positive entry to debug
    # lines.append('  10.10.10.10              dc-4a-3e-78-30-20     dynamic   \r')
    iptomac = dict()
    for line in lines:
        line = line.split()
        if line[MAC] in iptomac.keys() and line[MAC] != 'ff-ff-ff-ff-ff-ff':
            ip = iptomac[line[MAC]]
            print(f'arp poisoning detected! both {line[IP]} and {ip} both resolve as {line[MAC]}')
        iptomac.update({line[MAC]:line[IP]})
    
    # Hot detect ARP poisonings
    while True:
        packet = sniff(filter='arp', count=1)
        print(packet.summary())
    '''
    sniff(prn=arp_monitor, filter="arp", store=0)




    
if __name__ == '__main__':
    main()
