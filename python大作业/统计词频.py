# -*- coding: utf-8 -*-
import math
import re

def allwords(file_name,array):
    words_dict  = {}
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
    for k,v in words_dict.items():
        array.append(k)
    return 0
def wordfrequency(file_name,word):
    with open(file_name, 'r') as f:
        words_dict  = {}
        lines_list   = []
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
    for k,v in words_dict.items():
        if k==word:
            return v
    return 0
    
def xiangsidu(xl1,xl2):
    add=0
    square1=0;
    square2=0;
    for i in range(0,len(xl1)):
        add+=xl1[i]*xl2[i]
        square1+=xl1[i]*xl1[i]
        square2+=xl2[i]*xl2[i]
    print "相似度",add/(math.sqrt(square1)*math.sqrt(square2))
    return 0
def xiangliang(file_name1,file_name2,xl1,xl2,array):
    for i in array:
        xl1.append(wordfrequency(file_name1,i))
    print
    for i in array:   
        xl2.append(wordfrequency(file_name2,i))
    xiangsidu(xl1,xl2)
file_name1 = 'test.txt'
file_name2 = 'test2.txt'
array=[]
allwords(file_name1,array)
allwords(file_name2,array)
array=list(set(array))
xl1=[]
xl2=[]
xiangliang(file_name1, file_name2,xl1,xl2,array)



