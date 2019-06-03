# -*- coding: utf-8 -*
import os
import sys

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        f = open(dir)
        iter_f = iter(f)
        str = ""
        for line in iter_f:
            str = str + line
        find_all = True

        for keyword in sys.argv[1:]:
            if(str.find(keyword) == -1):
                find_all = False
                break

        if find_all == True:
            fileList.append(f)
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList



def main():
    if len(sys.argv) == 1:
        print 'please input key word in the cmd line'
        print 'example: python multisearch key1 key2'
        return 1
    list = GetFileList('./', []) 
    for e in list:
        print e.name

if __name__ == '__main__':
   main()