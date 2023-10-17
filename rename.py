import os
path=input('请输出文件路径(结尾加上/):')

# 获取该目录下所有文件，存储列表
fileList = os.listdir(path)

n = 0

for i in fileList:

    # 设置旧文件名
    oldname = path + os.sep + fileList[n]
    

    # 设置新文件名
    newname = path + os.sep + 'a'+str(n+1)+'.'