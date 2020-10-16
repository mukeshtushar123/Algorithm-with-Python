#!/usr/bin/env python
# coding: utf-8

# In[33]:


from collections import deque
bride = "rmrm"
groom = "mmmr"
bride_list = list(bride[::-1])
groomlist = deque(groom)
status = False
for i in range(len(bride_list)):
    for j in range(len(groomlist)):
        if bride_list[-1] == groomlist[0]:
            bride_list.pop()
            groomlist.popleft()
            status=True
            break
        else:
            groomlist.rotate(-1)
            status=False
    if status==False:
        break
print(len(groomlist))    

