#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Se Importa las librerias
import pandas as pd
import numpy as np


# In[20]:


lista = [1, 3, 5, 6, 10, 10]
indice = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6'] # Indices
serie = pd.Series(data=lista, index=indice) # Creando serie desde una lista
print(serie)


# In[6]:


serie['n2'] # Elemento de una serie proporcionando indice


# In[7]:


serie[1] # Accediendo al elemento con su posicion.


# In[8]:


serie.size # Tamaño de la serie


# In[9]:


len(serie)

serie.index
# In[11]:


serie.dtype


# In[14]:


serie.count()


# In[17]:


serie.sum() # Suma de los elementos


# In[19]:


serie.cumsum() # Suma acumulada


# In[25]:


f = serie.value_counts() # Frecuencia de los elementos en la serie


# In[28]:


f[1]


# In[29]:


serie.min() # Valor minimo de la serie


# In[30]:


serie.max() # Valor Maximo de la serie


# In[31]:


serie.mean() # Promedio de los elementos de la serie


# In[32]:


serie.std()


# In[37]:


serie.describe()


# In[36]:


des['mean']


# In[ ]:




