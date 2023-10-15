#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def matrix_operations(matrix):
 min_element = np.min(matrix)
 max_element = np.max(matrix)
 print("Minimum element:", min_element)
 print("Maximum element:", max_element)
 trace = np.trace(matrix)
 print("Trace:", trace)
 rank = np.linalg.matrix_rank(matrix)
 print("Rank:", rank)
 eigenvalues, eigenvectors = np.linalg.eig(matrix)
 print("Eigenvalues:", eigenvalues)
 print("Eigenvectors:", eigenvectors)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_operations(matrix)


# In[ ]:




