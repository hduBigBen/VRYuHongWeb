#!/user/bin/env python
# -*- coding:utf-8 -*-

import socket
import ReadAndWrite

def client(ip, fileName):
    # 待建立连接HOST的ip/port
    # ip_port = ('172.23.241.191', 9999)
    ip_port = (ip, 9999)
    # 建立socket
    s = socket.socket()
    # 建立连接
    s.connect(ip_port)
    while (True):
        # 待发送的信息
        # send_data = input('给对方发送信息：').strip()
        # s.send(bytes(send_data, encoding='utf-8'))

        # 接收信息并显示
        recv_data = s.recv(1024)
        if(str(recv_data, encoding='utf-8') != ''):
            print(fileName, str(recv_data, encoding='utf-8'))
            ReadAndWrite.write(fileName, str(recv_data, encoding='utf-8'))

    s.close()