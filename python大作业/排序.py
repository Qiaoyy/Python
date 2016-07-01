# import operator  
# x = {1:2, 3:4, 4:3, 2:1, 0:0}  
# sorted_x = sorted(x.iteritems(), key=lambda x : x[1], reverse=True)  
# print sorted_x
d={}
aaa = "E:\\testFile\\AAA.txt"

with open(aaa, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line