# !/user/bin/env python
# -*- coding:utf-8 -*-

import socket
import time
import osPath
import win32api
import getTime
import ReadAndWrite


# 待bind的ip/port
ip_port = ('192.168.6.81', 9999)
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
            # thisTime = getTime.getTime()  # 这次修改的时间
            thisTime = getTime.getFileSize("C:\VideoSample")
            lastTime = ReadAndWrite.read('time.txt')  # 上次修改的时间
            # print(thisTime)
            # print(lastTime)

            if (str(thisTime) != str(lastTime)):
                print('thisTame', thisTime)
                # print('lastTame', lastTime)
                win32api.ShellExecute(0, 'open', r'C:\WindowsNoEditor\VR_Test.exe', '', '', 1)
                print('wangkai')
                ReadAndWrite.write('time.txt', str(thisTime))
                time.sleep(2)
                print('sabhska')


            isRxist = osPath.isExist()  # isRxist = 1 说明空闲

            if(isRxist == 1):
                print(isRxist)
                osPath.removePath()
                send_data = '1'
                conn.send(bytes(send_data, encoding='utf-8'))
        except Exception:
            time.sleep(2)

            thisTime = getTime.getTime()  # 这次修改的时间
            lastTime = ReadAndWrite.read('time.txt')  # 上次修改的时间
            # print(thisTime)
            print('two1')

            if (str(thisTime) != str(lastTime)):
                # win32api.ShellExecute(0, 'open', r'C:\WindowsNoEditor\VR_Test.exe', '', '', 1)
                win32api.ShellExecute(0, 'open', r'D:\soft\WebStorm 2018.1.5\bin\webstorm64.exe', '', '', 1)
                ReadAndWrite.write('time.txt', str(thisTime))
                # time.sleep(2)
                print ('two')


            isRxist = osPath.isExist()  # isRxist = 1 说明空闲
            if (isRxist == 1):
                osPath.removePath()
                send_data = '1'
                conn.send(bytes(send_data, encoding='utf-8'))
    conn.close()
