#!/usr/bin/python3
# coding: UTF-8

import sys
from scapy.all import IP, TCP, sr1

target_ip = sys.argv[1]
target_port = int(sys.argv[2])

ip_layer = IP(dst=target_ip)

# SYNパケットを作成する
syn_packet = ip_layer/TCP(dport=target_port, flags='S')

# SYNパケットを送信し、レスポンスを取得する
print('Send SYN packet:')
response_packet = sr1(syn_packet)
print(f'Response: {response_packet}')
print('-----------------------------------')

# SYN/ACKパケットが返ってきた場合、ACKパケットを送信する
if (response_packet.haslayer(TCP) and
    response_packet[TCP].flags == 'SA'):
    tcp_layer = TCP(dport=target_port, flags='A',
                    ack=response_packet.seq + 1,
                    seq=response_packet.ack)
    ack_packet = ip_layer/tcp_layer
    print('Send ACK packet:')
    response_after_handshake = sr1(ack_packet, timeout=3)
    print(f'Response: {response_after_handshake}')
    print('-----------------------------------')
    print(f'TCP port {target_port} is open')

# RSTパケットが返ってきた場合、ポートは閉じていると判断する
else:
    print(f'TCP port {target_port} is closed')
