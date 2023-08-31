#!/usr/bin/python3
# coding: UTF-8

import socket
import sys

target_ip = sys.argv[1]
target_port = int(sys.argv[2])

s = socket.socket()
errno = s.connect_ex((target_ip, target_port))
s.close()

if errno == 0:
    print(f"TCP port {target_port} is open")
else:
    print(f"TCP port {target_port} is closed")