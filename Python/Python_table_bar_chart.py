#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Data_CSV.csv')
Father = 'Father'
FatherData = data[data['Family Members'] == Father]
Barchart = FatherData.groupby([FatherData['Year Month'],
            FatherData['Family Members']])['Allowance'].sum()
print(Barchart)
plt.title("Total Father Allowance")
Barchart.plot(kind='bar',figsize=(8,4))


# In[ ]:




