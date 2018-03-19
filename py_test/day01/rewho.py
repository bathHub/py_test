import re
import os

f1=os.popen('who','w')
f=open('who.txt','r')
for i in f1:
    print(re.split('\s\s+|\t',i.rstrip()))

f.close()
