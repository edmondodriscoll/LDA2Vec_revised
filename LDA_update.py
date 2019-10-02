#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

import datetime
datetime_object = datetime.datetime.now()
# print(datetime_object)

import random
list =[]
for x in range(1):
    y= random.randint(1,3)
    list.append(y)

df = pd.DataFrame(list, columns = ["test"])

from datetime import datetime, timedelta
n= datetime.strftime(datetime.now() + timedelta(random.randint(0,2)), '%Y-%m-%d')


n

df.to_csv("update{}".format(n))

print("ran to the end")

