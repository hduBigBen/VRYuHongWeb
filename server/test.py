# coding=utf-8

import ReadAndWrite
import getTime


thisTime = getTime.getTime()  # 这次修改的时间
print(thisTime)

print(getTime.getFileSize("C:\VideoSample"))
# ReadAndWrite.write('time.txt', str(thisTime))
# lastTime = ReadAndWrite.read('time.txt')



