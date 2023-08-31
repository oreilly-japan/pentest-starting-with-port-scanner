#!/usr/bin/python3
# coding: UTF-8

from scapy.all import sniff

# sniff関数の引数に指定するコールバック関数
def print_packet(packet):
    packet.show()

sniff(filter='icmp', prn=print_packet, count=5)
