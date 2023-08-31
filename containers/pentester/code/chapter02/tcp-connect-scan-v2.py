#!/usr/bin/python3
# coding: UTF-8

import sys
import time

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
    ack_tcp_layer = TCP(dport=target_port, flags='A',
                        ack=response_packet.seq + 1,
                        seq=response_packet.ack)
    ack_packet = ip_layer/ack_tcp_layer
    print('Send ACK packet:')
    sr1(ack_packet, timeout=3)
    print('-----------------------------------')
    print(f'TCP port {target_port} is open')

    # 接続を終了するためにFINパケットを送信する
    print('Send FIN packet:')
    fin_tcp_layer = TCP(dport=target_port, flags='FA',
                        ack=response_packet.seq + 1,
                        seq=response_packet.ack)
    fin_packet = ip_layer/fin_tcp_layer
    response_fin_packet = sr1(fin_packet, timeout=3)
    print(f'Response: {response_fin_packet}')

    # FINパケットが返ってきた場合、ACKパケットを送信する
    if (response_fin_packet.haslayer(TCP) and
        response_fin_packet[TCP].flags == 'FA'):
        print('Send ACK packet:')
        ack_after_fin_tcp_layer = TCP(
            dport=target_port, flags='A',
            ack=response_fin_packet.seq + 1,
            seq=response_fin_packet.ack
        )
        ack_packet_after_fin = ip_layer/ack_after_fin_tcp_layer
        sr1(ack_packet_after_fin, timeout=3)
        print('Connection closed')
    else:
        print('Failed to close connection')

# RSTパケットが返ってきた場合、ポートは閉じていると判断する
else:
    print(f'TCP port {target_port} is closed')
