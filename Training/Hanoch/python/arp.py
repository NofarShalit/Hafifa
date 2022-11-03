import subprocess as sub


ARP_CMD = 'arp -a'
IP = 0
MAC = 1


def main():
    proc = sub.run(ARP_CMD, shell=False,
                   capture_output=True)
    lines = proc.stdout.decode().split('\n')[3:-1]
    '''add fake arp poisoning positive entry to debug''' 
    # lines.append('  10.10.10.10              dc-4a-3e-78-30-20     dynamic   \r')
    iptomac = dict()
    for line in lines:
        line = line.split()
        if line[MAC] in iptomac.keys() and line[MAC] != 'ff-ff-ff-ff-ff-ff':
            ip = iptomac[line[MAC]]
            print(f'arp poisoning detected! both {line[IP]} and {ip} both resolve as {line[MAC]}')
        iptomac.update({line[MAC]:line[IP]})
            
        

    
if __name__ == '__main__':
    main()
