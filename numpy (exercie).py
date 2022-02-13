#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Écrivez un programme Python pour convertir un tableau en une liste ordinaire avec les mêmes éléments.
'''
import numpy as np

a = np.array([[1,2,3]])
b = np.array([[1,2,3],[4,5,6]])

print(a.tolist())
print(b.tolist())


# In[3]:


'''Écrivez un programme NumPy pour calculer la somme des éléments diagonaux d'un tableau donné.'''
import numpy as np 
  
n_array = np.array([[15, 25, 15], 
                    [30, 20, 2], 
                    [11, 45, 30]])

trace = np.trace(n_array) 
print(trace)


# In[20]:


'''Étant donné un tableau de votre choix, obtenez toutes les valeurs supérieures à X :

si a = [[1,2],[3,5]] et x = 2 : alors 3 et 5 sont supérieurs à 2.'''
b = np.array([[1,2],[3,5]])
x = 2 
print(b[b>x])


# In[33]:


'''Étant donné deux tableaux, A et B ont la même forme. 

La tâche consiste à appliquer l'addition à la main : C est le nouveau tableau.'''

a = np.array([1,2,3])
b = np.array([4,5,6])
c=a+b

print (c)



# In[36]:


'''Écrivez un programme NumPy pour soustraire la moyenne de chaque ligne d'une matrice donnée.'''

A = np.array([[15, 25, 15], 
                    [30, 20, 2], 
                    [11, 45, 30]])

n=np.shape(A)
l=n[0]
c=n[1]
B=np.zeros(l*c).reshape(l,c)
m=np.mean(A,axis=1)

for i in range(0,l):
    for j in range(0,c):
        B[i,j]=A[i,j]-m[i]
print(B)


# In[ ]:




