
import re
# txt = open("123.txt", "r").read()
# def three_same_be(word_file):
#     print word_file
#     count=0
#     for w in word_file:
#         if len(w)>3 and w[0]==w[-1]:
#             print w
#             count+=1
#     print count
#  
#  
# 
# three_same_be(txt)
file_name = '123.txt'
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
    if k=='a':
        print v