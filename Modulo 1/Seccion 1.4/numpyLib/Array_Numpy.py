#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np


# In[7]:


lista = [1, 2, 3, 4, 5]
vector = np.array(lista)

print(lista)
print(vector)


# In[8]:


lista * 5


# In[9]:


vector * 5


# In[10]:


lista_result = list()
for i in lista:
    lista_result.append(i * 5)
print(lista_result)


# In[11]:


vector_sum = np.sum(lista)
print(vector_sum)


# In[13]:


vector_prom = np.mean(lista)
print(vector_prom)


# In[14]:


vector + vector


# In[15]:


lista + lista


# In[17]:


lista1 =[4, 7, 9, 1.4, -5]

vector1 = np.array(lista1)

vector + vector1


# In[18]:


vector[2]


# In[19]:


for i in vector:
    print(i)


# In[30]:


# Slices o Rebanadas, rodajas

print(vector[3])
print(vector[1:4])
print(vector[1:])
print(vector[:4])
print(vector[:])


# In[32]:


# Vector de solo ceros

vector_z = np.zeros(5)
print(vector_z)


# In[33]:


# Vector de solo unos
vector_o = np.ones(5)
print(vector_o)


# In[35]:


# Creación de una Matríz
lista_py = [[1, -4], [12, 3], [7.2, 5]]
matriz = np.array(lista_py)
print(matriz)
print(lista_py)


# In[38]:


# Dimensionamiento de una matriz
# Creando una matriz de ceros
dimension = (5, 2)
matriz_z = np.zeros(dimension)
print(matriz_z)


# In[70]:


# Creando una matriz de Unos
dim = (3, 2)
matriz_o = np.ones(dim)
print(matriz_o)


# In[40]:


# Copia de una matriz
matriz_copia = np.copy(matriz)
print(matriz_copia)


# In[44]:


# Acceder a los valores de una matriz

# acceder a elementos individuales
print(matriz_copia[0,1])
print(matriz_copia[2,0])
print(matriz_copia[1, 1])
print(matriz_copia[1, 0])


# In[50]:


print(matriz_copia)
matriz_copia[2,0] = 16
print(matriz_copia)

matriz_copia[2,0]= matriz_copia[2,0]/2
print(matriz_copia)


# In[51]:


print(matriz_copia[1,:])


# In[52]:


# Imprimir columnas
print(matriz_copia[:,0])


# In[53]:


print(matriz_copia[0:2,:])


# In[54]:


print(matriz_copia[1:3,:])


# In[55]:


lista_dato = [[12, 8], [15, 20], [30, -6]]
m = np.array(lista_dato)
print(m)


# In[59]:


m[1,:] = m[1,:] - 4
print(m)


# In[62]:


lista_d=[[12, 8],[15,20],[30,-6]]
n=np.array(lista_d)
print(n)
# Restando -4 a toda la fila
print(n[1,:]-4) 
print(n)


# In[64]:


lista_dato = [[12, 8], [15, 20], [30, -6]]
m = np.array(lista_dato)
print(m)

# Restando -4 a toda la fila
m[1,:] = m[1,:]-4
print(m)

