import os
import time


def getTime():
    # 读取目录的时间
    t = os.stat('C:\VideoSample\VideoSample.mp4')
    return time.localtime(t.st_ctime)
    # print(t)
    # print("修改时间:", t.st_mtime)
    # print(time.localtime(t.st_mtime))
    # print("创建时间?", time.localtime(t.st_ctime))
    # print("访问时间：", time.ctime(t.st_atime))





def getFileSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
            # print(f)
    return size
