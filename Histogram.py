#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')
pokemon = pd.read_csv("pokemon.csv")
print(pokemon.shape)
pokemon.head(15)


# In[10]:


basecolor = sb.color_palette()[0]
plt.hist(data = pokemon, x = "speed", color = basecolor, bins = 20)


# In[ ]:




