# -*- coding: utf-8 -*-

import re
import requests
import BeautifulSoup
import urllib2
i=0
import os
import math
def nsfile(i,testnote):
    b = os.path.exists("E:\\testFile\\")
    if b:
        print "File Exist!"
    else:
        os.mkdir("E:\\testFile\\")
    filename = "E:\\testFile\\"+str(i+1)+".txt"
    f = open(filename,'ab')
    f.write(testnote)
    f.close()

    print "file"+" "+str(i+1)+".txt"
#判断网页是否有效
def url(a):
    global i
    global num_url
    try:  
        page = urllib2.urlopen(a)
        num_url.append(a)
        print a
    except:  
        print "无效连接",a 
#爬取网页文本内容
def crawl(i,a):
    page = urllib2.urlopen(a)
    html_doc = page.read()
    soup = BeautifulSoup.BeautifulSoup(html_doc)
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    soup.prettify()
    reg1 = re.compile("<[^>]*>")
    content = reg1.sub('',soup.prettify())
    clean_str = re.sub(r'\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020', '', str(content)) 
    clean_str=re.sub(" +", " ", str(clean_str))
    clean_str.strip()
    nsfile(i,clean_str)
def allwords(file_name,array,words_dict):
    lines_list   = []
    with open(file_name, 'r') as f:
        for line in f:
            match = re.findall(r'[^a-zA-Z0-9]+', line)
            for i in match:
                line = line.replace(i, ' ')
            lines_list = line.split()
            for i in lines_list:
                if i not in words_dict:
                    words_dict[i] = 1
                else:
                    words_dict[i] = words_dict[i] + 1
    for k in words_dict:
        array.append(k)
    return 0

def cosine(xl1,xl2):
    add=0
    square1=0;
    square2=0;
    for i in range(0,len(xl1)):
        add+=xl1[i]*xl2[i]
        square1+=xl1[i]*xl1[i]
        square2+=xl2[i]*xl2[i]
    return add/(math.sqrt(square1)*math.sqrt(square2))
def vector(file_name1,file_name2,array,words_dict1,words_dict2):
    xl1=[]
    xl2=[]
    for i in array:
        try:
            xl1.append(words_dict1[i])
        except:
            xl1.append(0)
    for i in array:   
        try:
            xl2.append(words_dict2[i])
        except:
            xl2.append(0)
    return cosine(xl1,xl2)
def similar(file_name1,file_name2):
    array=[]
    words_dict1={}
    words_dict2={}
    allwords(file_name1,array,words_dict1)
    allwords(file_name2,array,words_dict2)

    array=list(set(array))
    return vector(file_name1, file_name2,array,words_dict1,words_dict2)


r = requests.get('http://english.jxufe.edu.cn/')
data = r.text
link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
num_url=[]
top="http://english.jxufe.edu.cn/"
num_url.append(top)
for k in link_list:
    if k[0]=="/":
        k=top+k
        putin=k
    url(putin)
num_url=list(set(num_url))
i=0
with open("E:\\testFile\\url.txt", 'w') as f:
    for a in num_url:
        crawl(i,a)
        f.write(a+"\n")
        i=i+1
        
        
sort={}
for m in range(1,45):
    add=0
    for n in range(1,45):
        file_name1 = "E:\\testFile\\"+str(m)+'.txt'
        file_name2 = "E:\\testFile\\"+str(n)+'.txt'
        add+=similar(file_name1,file_name2)
    sort[m]=add
sorted_x = sorted(sort.iteritems(), key=lambda x : x[1], reverse=True)
haha=[]
for k,v in sorted_x:
    haha.append(k)

flag={}
select={}
list1={}
k=1
with open("E:\\testFile\\url.txt", 'r') as f:
    line = f.readlines() 
    for i in line:
        i=i.strip('\n')
        flag[k]=i
        k=k+1
for j in range(1,5):
    for n in haha:
        if flag.has_key(n):
            for m in range(1,45):
                if flag.has_key(m):
                    file_name1 = "E:\\testFile\\"+str(n)+'.txt'
                    file_name2 = "E:\\testFile\\"+str(m)+'.txt'
                    select[file_name2]=similar(file_name1,file_name2)
                    if select[file_name2]>=0.90:
                        with open("E:\\testFile\\list"+str(j)+".txt", 'a') as f:
                            f.write(flag[m]+'\n')
                        del flag[m]
            break;   
for i in range(1,45):
    if flag.has_key(i):
        with open("E:\\testFile\\list5.txt", 'a') as f:
            f.write(flag[i]+'\n')
