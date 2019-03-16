# -*- coding:utf-8 -*-

import web
import ToVideo
import main
import client
import FTP
import ReadAndWrite

urls = (
    '/start', 'start',  # 开启相机服务
    '/client1', 'client1',  # socket服务监听
    '/client2', 'client2',
    '/client3', 'client3',
    '/client4', 'client4',
    '/hello[/]?.*', 'hello',
    '/fun2', 'fun2',
    '/fun3', 'fun3',
    '/fun4', 'fun4',
    '/openServer', 'openServer',


)

app = web.application(urls, globals())
render = web.template.render('templates')


# global number
# number = 1
class start:
    def GET(self):

        main.videoFaceDet()

class client1:
    def GET(self):
        ReadAndWrite.write('1.txt', '1')
        # client.client('192.168.43.140', '1.txt')
        client.client('192.168.1.100', '1.txt')
class client2:
    def GET(self):
        ReadAndWrite.write('2.txt', '1')
        client.client('192.168.1.102', '2.txt')

class client3:
    def GET(self):
        ReadAndWrite.write('3.txt', '1')
        client.client('192.168.1.103', '3.txt')

class client4:
    def GET(self):
        ReadAndWrite.write('4.txt', '1')
        client.client('192.168.1.104', '4.txt')

class openServer:
    def GET(self):
        return render.index_9()




class hello:
    def GET(self):
        return render.index()
class fun2:
    def GET(self):
        return render.index_2()


class fun3:
    def GET(self):
        return render.index_3()


class fun4:
    def GET(self):
        ToVideo.imagetovideo()
        number = ReadAndWrite.read('1.txt')
        if (number == '1'):  # 1空闲
            ReadAndWrite.write('1.txt', '0')
            FTP.ftp_upload('192.168.1.100')
            return render.index_4()
        else:
            number = ReadAndWrite.read('2.txt')
            if (number == '1'):
                ReadAndWrite.write('2.txt', '0')
                FTP.ftp_upload('192.168.1.102')
                return render.index_5()
            else:
                number = ReadAndWrite.read('3.txt')
                if (number == '1'):
                    ReadAndWrite.write('3.txt', '0')
                    FTP.ftp_upload('192.168.1.103')
                    return render.index_6()
                else:
                    number = ReadAndWrite.read('4.txt')
                    if (number == '1'):
                        ReadAndWrite.write('4.txt', '0')
                        FTP.ftp_upload('192.168.1.104')
                        return render.index_7()
                    else:
                        return render.index_8()
if __name__ == "__main__":
    app.run()
