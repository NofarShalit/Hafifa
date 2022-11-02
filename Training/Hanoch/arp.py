import subprocess as sub


ARP_CMD = 'arp -a'
IP = 1
MAC = 2


def main():
    proc = sub.run(ARP_CMD, shell=False,
                   capture_output=True)
    lines = proc.stdout.decode().split('\n')[3:-1]
    iptomac = dict()
    print(lines)
    for line in lines:
        line = line.split(' ')
        if line[MAC] in iptomac.values():
            iptomac.update({line[IP]:line[MAC]})
        

    
if __name__ == '__main__':
    main()
