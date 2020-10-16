#!/usr/bin/env python
# coding: utf-8

# In[71]:


N = int(input())
num =[int(x) for x in input().split()]
binary=[]
dictionary = {}
for i in range(N):
    binary.append(bin(num[i]).replace("0b", ""))
index = num.index(max(num))
maxdigit = len(binary[index]) 
for i in range(N):
    dictionary[num[i]] =[binary[i].count("0")+(maxdigit-len(binary[i])),binary[i].count("1")]
count = 0
for i in range(N):
    for j in range(i+1,N+1):
        possible = num[i:j]
        total0=0
        total1=0
        for k in range(len(possible)):
            total0 =total0 + dictionary[possible[k]][0]
            total1 =total1 + dictionary[possible[k]][1]
        if total0 == total1:
            count = count+1

res =bin(count).replace("0b", "")
leftjoin = (maxdigit-len(res))*"0"
print(leftjoin+res)

