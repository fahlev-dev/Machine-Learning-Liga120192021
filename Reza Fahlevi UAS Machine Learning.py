#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Membaca cvs
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Liga120192021.csv')
print (df.to_string())


# In[3]:


#Menggambar plot grafik garis
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Liga120192021.csv')
df.plot()
plt.show()


# In[5]:


#Mendapatkan modus dari tiap kolom
from scipy import stats
df = pd.read_csv('Liga120192021.csv')
x = stats.mode(df, keepdims=True)
print(x)


# In[7]:


#Menggambar scattered plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  
#baca data csv
df = pd.read_csv('Liga120192021.csv')
sns.scatterplot(data = df)
plt.show()


# In[ ]:




