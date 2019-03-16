# FTP操作
import ftplib
import datetime


def ftp_upload(host):
    # host = '172.23.241.191'
    username = ''
    password = ''
    f = ftplib.FTP(host)
    f.login(username, password)  # 登录

    file_remote = 'VideoSample'
    file_local = 'VideoSample.mp4'
    bufsize = 102400  # 设置缓冲器大小
    fp = open(file_local, 'rb')
    fp2 = open(file_local, 'rb')
    f.storbinary('STOR ' + file_remote+'.mp4', fp, bufsize)
    f.cwd('/a/')  # 设置FTP路径
    now_time = datetime.datetime.now()
    time1_str = datetime.datetime.strftime(now_time, '%Y%m%d%H%M%S')
    f.storbinary('STOR ' + file_remote + time1_str + '.mp4', fp2, bufsize)
    fp.close()
    f.quit()


