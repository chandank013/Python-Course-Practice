# python -m pip install numpy:
import numpy as np

# ar = np.array(12)  # (1D)
# print(ar)

# ar1 = np.array([1,3,5,7,9])    # (1D)
# print(ar1)

# ar2 = np.array([[1,3,5,7,9],[2,4,6,8,10]])    # (2D)
# print(ar2)

# ar3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])    # (3D)
# print(ar3)
# print(ar3.ndim)    # Show the dimention of the array

# ar1 = np.array([1,3,5,7,9],ndmin= 3)    # Here through ndim we create array dimention as we want
# print(ar1)
# print(ar1.ndim)   # It show the the dimention of the array as we mention avobe



# # NumPy Attributes:

# ar1 = np.array([1,3,5,7,9])
# ar2 = np.array([[1,3,5],[2,4,6]])
# ar3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) 
# ar4 = np.array([1,3,5,7],ndmin= 4) 

# print(ar1.ndim)
# print(ar3.ndim)

# print(ar3.shape)
# print(ar4.shape)

# print(ar1.dtype)
# print(ar1.itemsize)
# print(ar1.itemsize)
# print(ar1.nbytes)

# ar5 = np.array([1.1,2.2,3.3])
# print(ar5)
# print(ar5.dtype)



# Few more method to learn about Creating an Array:

#01 np.zeros():  # it create an array of single dimentions filled with zero

# ar = np.zeros(3)
# print(ar)  
# print(ar.dtype)  

# ar1 = np.zeros((4,4))   # 2D Array filled with zero of three rows and four columns
# print(ar1)   

# ar3 = np.zeros((3,4,5))   # 3D Array filled with zero of three plans , rows and coloumns 
# print(ar3) 
 

#02 np.ones():  # same as np.zeros(4) it form array filled with 1

# ar4 = np.ones((3,4,5))   # 3D Array filled with zero of three plans , rows and coloumns 
# print(ar4) 
 

#03 np.empty(): # it create an empty array in witch element may be anything filled with anything (mean garbage value)

# ar = np.empty(4)
# print(ar)

# ar1 = np.empty((3,4))
# print(ar1)


# #04 np.eye():  # It used to form identity metrix

# ar4 = np.eye(3)
# print(ar4)

# ar2 = np.eye(4)
# print(ar2)

# ar2 = np.eye(4,3)  # it does not give all diagonal elements 1 becouse it is not a square matrics
# print(ar2)

# ar2 = np.eye(4,2)  # no a identity metrix for identity metricx we have to give onle one parameter
# print(ar2)


# #05 np.diag([l,m,nx...xz]):  # it give matrics of lxmxn having elements (l,m,n,...,z in each row diagonally) rest elements are zero 

# ar = np.diag([2,3])
# print(ar)

# ar = np.diag((2,3,5,6))  # also work for tuple
# print(ar)


#06 np.arange(start,end,step):   # range functin covert the digit between two number in to array

# ar = np.arange(0,11)
# print(ar)

# ar = np.arange(0,48,3)
# print(ar)

# ar1 = np.arange(-10,0,2)
# print(ar1)


#07 np.linespace(start,end,num = 5)  # It create an array of elements five and elements belong to between the start and end, diff between two elements would be equal (diff = (start + end)/(num - 1))

# ar1 = np.linspace(0,10,num = 5)
# print(ar1)

# ar1 = np.linspace(13,50,num = 6)
# print(ar1)
