#coding=utf-8 
print '依次输入第一个矩形中心的x坐标和 y坐标以及它们的宽和高'
centerx1=input()
centery1=input()
w1=input()
h1=input()
x1=centerx1-w1
x2=centerx1+w1
y1=centery1-h1
y2=centery1+h1
print '依次输入第二个矩形中心的x坐标和 y坐标以及它们的宽和高'
centerx2=input()
centery2=input()
w2=input()
h2=input()
x3=centerx2-w2
x4=centerx2+w2
y3=centery2-h2
y4=centery2+h2
def  judge(x1,x2,x3,x4):
    if((x3>x1 and x3<x2 and x4>x2)|(x4>x1 and x4<x2 and x3<x1)):
        return 1
    if(x3>=x1 and x4<=x2):
        return 2
    if(x3<=x1 and x4>=x2):
        return 3
    return 0
a=judge(x1,x2,x3,x4)
b=judge(y1,y2,y3,y4)
flag=0
if((a==1 and b==1)or((a==2 or a==3) and b==1)or (a==1 and(b==2 or b==3))or(a==2 and b==3)or(a==3 and b==2)):
    print'相交'
    flag=1
if((a==2 and b==2)or (a==3 and b==3)):
    print'重叠'
    flag=1
if(flag==0):
    print '分离'



