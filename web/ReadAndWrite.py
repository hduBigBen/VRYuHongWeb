def read(fileName):
    f = open(fileName, 'r')
    return f.read()



def write(fileName,i):
    f = open(fileName, 'w')  # 若是'wb'就表示写二进制文件
    f.write(i)
    f.close()
