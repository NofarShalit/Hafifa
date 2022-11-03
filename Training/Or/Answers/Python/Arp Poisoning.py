from scapy.all import *
import os, re

REGEX = r'([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)'

def main():
    with os.popen("arp -a") as f:
        arp_table = f.read()
    arp_table = arp_table.split("\n\n")

    for interface in arp_table:
        for line in re.findall(REGEX,interface):
            for line2 in re.findall(REGEX,interface):
                if line[1] == line2[1] and line[0] != line2[0]:
                    spoofed = True
                    break
        if spoofed:
            print("arp table is spoofed")
        else:
            print("arp table is not spoofed")
        spoofed = False

if __name__ == "__main__":
    main()