#coding=utf-8 
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
num= 0 
flag=2
while(num<100):
    if isPrime(flag)==True:
        temp = "%d"%flag;
        str1 = temp[::-1];
        if temp!=str1:
            if isPrime(int(str1))==True:
                print "%4s "%(flag),
                num=num+1
                if num%10==0:
                    print 
    flag+=1
 
   
    
       
