#coding=utf-8 

import math
class QuadraticEquation(object):
    def __init__(self,a,b,c):  
        self.__a=a
        self.__b=b
        self.__c=c
    def get_a(self):  
        return self.__a  
    def get_b(self):  
        return self.__b  
    def get_c(self):  
        return self.__c
    def getDescriminan(self):
        return  self.__b*self.__b-4*self.__a*self.__c
    def getRoot1(self):
        if self.getDescriminan()>=0:
            return (-self.__b+math.pow(self.getDescriminan(), 0.5))/(2*self.__a) 
        else:     
            return 0
    def getRoot2(self):
        if self.getDescriminan()>=0:
            return (-self.__b-math.pow(self.getDescriminan(), 0.5))/(2*self.__a) 
        else:     
            return 0

a=input()
b=input()
c=input()
A = QuadraticEquation(a,b,c)    
print '该方程的两个根分别为：',A.getRoot1(),A.getRoot2()
