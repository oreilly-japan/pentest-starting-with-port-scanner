#!/usr/bin/python3
# coding: UTF-8

import sys
from scapy.all import IP, TCP, sr1

target_ip = sys.argv[1]
target_port = int(sys.argv[2])

# SYNパケットを作成する
syn_packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")

# パケットを送信し、レスポンスを取得する
response_packet = sr1(syn_packet)

# SYN/ACKパケットが返ってきた場合は、ポートが開いていると判断
if (response_packet.haslayer(TCP) and 
    response_packet[TCP].flags == "SA"):
    print(f"TCP port {target_port} is open")
else:
    print(f"TCP port {target_port} is closed")