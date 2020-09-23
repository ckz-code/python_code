import os
import shutil


# 批量提取doc以及docx文件

# 提取位置：
# 目录
#    |目录1
#         |目录2

# 只提取到目录1层次

def getdoc(path1,path2):

    for root,dirs,files in os.walk(path1):
        break
    for file in files:   
        if file.endswith(".doc") or file.endswith(".docx"):
            docpath=os.path.join(root,file)
            shutil.copy(docpath,path2)

    print("-------------目录------------")
    print(dirs)
    print("-----------------------------")

    for dir in dirs:
        path3=root+"\\"+dir
        for filename in os.listdir(path3):
            print(filename)
            if filename.endswith(".doc") or filename.endswith(".docx"):
                docpath=os.path.join(path3,filename)
                shutil.copy(docpath,path2)

sopath=r"E:\工作文件\2020护网（网安）"
depath=r"E:\code\python_code\doc"
getdoc(sopath,depath)