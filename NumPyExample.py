# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 14:09:25 2016

@author: Ravi
"""

import numpy as np
import copy
#List and list operation
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print(list1+list2)
#output is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int32)
print(x)
print(type(x)) # type of x is  numpy.ndarray
print(x.ndim) # ndim is dimension of the array
print(x.shape)
print(x.size)
print(x.dtype) # datatype is int32
print(x.itemsize)
print(x.data)
print(x[0])
print(x[0,2])
print(x[:,1])#First row
x[:,2]=[11,11,11]
print(x)

d=x.copy
print(id(d)==id(x))

x2=x;
print(id(x)==id(x2))
x3=copy.deepcopy(x)
print(id(x)==id(x3))

y=np.zeros(7)
print (y)

y=np.zeros(7) # float type
print (y)

k=np.zeros(7, dtype=np.int)
print(k)

m=np.arange(10)
print(m)
print(m*11.11)

a=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int32)
b=a
e=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(a+b)
print(a+e)

x=np.arange(20)
print(x)
indx=[1,5,6,14]
print(x[indx])

print (x.sum())
print(x.mean())
print(np.median(x))
print(x.std())
print(x.max())
print(x.min())
print(x.nonzero())

a=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int32)
print(a)
#Correlation Coefficient
print(np.corrcoef(a))
#Covarience
print(np.cov(a))
print(a.transpose())
np.invert(a)
print(a)

#Matrix
mat=np.mat([[1,9],[2,8]])
print(mat)

arr=np.array([[1,9],[2,8]])
mat=np.mat(arr)
print(arr)
print(mat)
print(arr*arr)
print(mat*mat)
print(mat.T)#Transpose of Matrix
print(mat.I) #Inverse Matrix
print((mat)*(mat.I)) #Identity Matrix

#Vectorizing Function

import math
def sinc(x):
    #for Vectorization Demo
    if x==0.0:
        return 1.0
    else:
        w=math.pi*x
    return math.sin(w)/w

from numpy import vectorize
vsinc=vectorize(sinc)
vsinc([1.3,1.5])
vsinc([1.3,1.5,1.6,1.7])
