import subprocess as sub

from scapy.all import *


ARP_CMD = 'arp -a'
IP = 0
MAC = 1

def arp_request(ip):
    req = Ether(src="ff:ff:ff:ff:ff:ff", dst="ff:ff:ff:ff:ff:ff") / ARP(psrc='1.2.3.4', pdst=ip)
    responses = srp(req, timeout=5, verbose=False)
    answer = responses[0][0][1]
    print(answer.show())
    
def arp_authenticate(pkt):
    if ARP in pkt and pkt[ARP].op == 2:
        claimedmac = pkt[ARP].hwsrc
        
    
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
    
    '''
    arp_request('10.0.0.1')
    sniff(prn=arp_authenticate, filter="arp", store=0)




    
if __name__ == '__main__':
    main()
