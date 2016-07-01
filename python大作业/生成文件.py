#coding=utf-8
'''
Created on 2012-5-29

@author: xiaochou
'''

import os
import time

def nsfile(s,testnote):
    '''The number of new expected documents'''
    #判断文件夹是否存在，如果不存在则创建
    b = os.path.exists("E:\\testFile\\")
    if b:
        print "File Exist!"
    else:
        os.mkdir("E:\\testFile\\")
    #生成文件
    for i in range(1,s+1):
        localTime = time.strftime("%Y%m%d%H%M%S",time.localtime())
        #print localtime
        filename = "E:\\testFile\\"+localTime+".txt"
        #a:以追加模式打开（必要时可以创建）append;b:表示二进制
        f = open(filename,'ab')
        f.write(testnote)
        f.close()
        #输出第几个文件和对应的文件名称
        print "file"+" "+str(i)+":"+".txt"
        time.sleep(1)
    print "ALL Down"
    time.sleep(1)

if __name__ == '__main__':
    s = input("请输入需要生成的文件数：")
    nsfile(s,'aaaa')
    