from pathlib import Path
import os

filePath = 'C:\WindowsNoEditor\VR_Test\Saved\SaveGames\end.sav'

def isExist():
    my_file = Path(filePath)
    if my_file.is_file():
        # 指定的文件存在
        # print('1')
        return 1
    else:
        return 0

def removePath():
    if os.path.exists(filePath):
        # 删除文件，可使用以下两种方法。
        os.remove(filePath)


