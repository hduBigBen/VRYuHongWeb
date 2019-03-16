# !/user/bin/env python
# -*- coding:utf-8 -*-

import socket
import time
import osPath

# 待bind的ip/port
ip_port = ('192.168.1.102', 9999)
# 建立socket
s = socket.socket()
# 绑定ip/port
s.bind(ip_port)
# 监听连接
s.listen()
print('等待用户连接中... ...')
while (True):
    # 建立连接后，将accept()返回元组赋值给conn, addr
    conn, addr = s.accept()
    if conn is not None:
        print('有一个用户已连接.\n等待对方发送信息.')

    while (True):
        try:

            isRxist = osPath.isExist()  # isRxist = 1 说明空闲

            if (isRxist == 1):
                print(isRxist)
                osPath.removePath()
                send_data = '1'
                conn.send(bytes(send_data, encoding='utf-8'))
        except Exception:
            print("diwsh")
            time.sleep(2)

            isRxist = osPath.isExist()  # isRxist = 1 说明空闲
            if (isRxist == 1):
                osPath.removePath()
                send_data = '1'
                conn.send(bytes(send_data, encoding='utf-8'))
    conn.close()
