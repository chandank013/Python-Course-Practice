# Array Indexing:

import numpy as np

# arr = np.array([2,4,8,10,12,24,26,20])
# print(arr[4])
# print(arr[-5])

# arr1 = np.array([[2,4,6,8],[1,3,5,7],[11,22,33,44],[10,20,30,40]])
# print(arr1[2,3])
# print(arr1[1,2])

# print(arr1[-2,-2])
# print(arr1[-2,-3])


# #01 arr[start:end:steps]
# arr = np.array([2,4,8,10,12,24,26,20])

# print(arr[::])    # it gives entire array
# print(arr[2:9:3])

# #02 arr[start:end:steps,start:end:steps]
# arr1 = np.array([[2,4,6,8],[1,3,5,7],[11,22,33,44],[10,20,30,40]])

# print(arr1[2])  # it gives [2,4,6,8]
# print(arr1[0:2])  
# print(arr1[0:3:2])   # it only act upon row

# print(arr1[:,0:2])    # it mean we want all the row and only two columns
# print(arr1[0:2,2:4])
# print(arr1[1:4:2,1:4:2])



#Reshaping of Array from 1D to 2D,1D to 3D,2D to 3D during reshaping it should be have sufficient number of elements

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# # print(arr.shape)   # it gives number of elements persent in an array
# ar = arr.reshape(3,4)  
# print(ar)  
# print(ar.shape)  

# ar = ar.reshape(4,3)     # (1D to 2D)
# print(ar)

# ar = ar.reshape(3,2,2)   # (1D to 3D)
# print(ar)


#ar.flatten() convert any dimention of array in to one dimention of array

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr.reshape(3,2,2)

print(arr.flatten())
print(arr.reshape(12))