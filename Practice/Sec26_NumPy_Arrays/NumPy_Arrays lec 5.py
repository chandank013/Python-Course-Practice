#NumPy Datatypes:

import numpy as np

# ar = np.array([1,2,3,4])
# print(ar.dtype)  # [int64]  it mean each integer containing (64/8) = 8 byte

# ar = np.array([1.2,2.0,3.5,4.6])
# print(ar.dtype)  # [floatt64]  it mean each integer containing (64/8) = 8 byte


# # How to mention a Byte:

#01 b-byte

# ar = np.array([1,2,3,127], 'b')   # if we take byte 'b' type of an array then we able to take elements between -128 to 127 if we take bigger number then its overflow
# print(ar)
# ar1 = np.array([1,2,3,128], 'b')   # JN
# print(ar1)
# print(ar.dtype)   # 8-bits = 1 byte


#02 B-unsigned byte

# ar1 = np.array([1,2,3,234], 'B')   # JN, allow only positive number between range (0 to 255).also follow cyclic ritation from both side
# print(ar1)
# ar2 = np.array([1,2,3,256], 'B')   # JN
# print(ar1)
# print(ar1.dtype)   #[uint]
# print(ar2.dtype)   


#03 i-integer

# ar1 = np.array([1,2,3,4], 'i')  #  JN
# print(ar1)    # 32 bits = 4 byte
# print(ar1.dtype)   



#04 I-integer

# ar1 = np.array([1,2,3,4], 'I')  #  JN
# print(ar1)    # 32 bits = 4 byte
# print(ar1.dtype)   



#05 f-float

# ar1 = np.array([1,2,3,4], 'f')  #  JN
# print(ar1)    # 32 bits = 4 byte
# print(ar1.dtype)   


#05 F-float

# ar1 = np.array([1,2,3,4], 'F')  #  JN convert in to array of complex number
# print(ar1)    # Complex64 = 4 bytes
# print(ar1.dtype)   


#06 o-object

# ar1 = np.array([1,2,3,4], 'O')  #  JN convert in to array of python object
# print(ar1)    
# print(ar1.dtype)   


#07 S-string

# ar1 = np.array([1,2,3,4], 'S')  #  JN convert in to array of string
# print(ar1)    # Complex64 = 4 byte
# print(ar1.dtype) 
# ar1 = np.array(['a','b','c','d'], 'S')  #  JN 
# print(ar1)   
# print(ar1.dtype)   


#08 U-Unicode

# ar1 = np.array([1,2,3,4], 'U')  #  JN convert in to array of unicode
# print(ar1)   
# print(ar1.dtype) 



# #Another method of creating Numpy array: These are not creating using symbol

# ar =np.array([1,2,3,4], 'int8')
# print(ar)
# print(ar.dtype)


# ar1 =np.array([1,2,3,4], 'int16')
# print(ar1)
# print(ar1.dtype)


# ar2 =np.array([1,2,3,4], 'int64')
# print(ar2)
# print(ar2.dtype)

# #'u' mean unsigned:

# ar =np.array([1,2,3,4], 'uint8')
# print(ar)
# print(ar.dtype)


# ar1 =np.array([1,2,3,4], 'uint16')
# print(ar1)
# print(ar1.dtype)


# ar2 =np.array([1,2,3,4], 'uint64')
# print(ar2)
# print(ar2.dtype)


# ar2 =np.array([1,2,3,4], 'float64')
# print(ar2)
# print(ar2.dtype)


ar2 =np.array([1,2,3,4], 'bool')    # any number other than 0 is positive in python
print(ar2)
print(ar2.dtype)

ar2 =np.array([1,2,0,4], '?') 
print(ar2)
print(ar2.dtype)

#int64 using longlong:

# ar2 =np.array([1,2,3,4], 'longlong')
# print(ar2)
# print(ar2.dtype)



