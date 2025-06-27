                            # list

list1 = [1,2,3,4,5]
list2 = list((1,2,3,4,5))
print(list2)


mylist = [23,53,6,8,4,567,5,56] # mutable
mylist[4] = 'ram'
print(mylist)


# mylist = [23,53,6,8,4,567,5,56] # Append method
# mylist.append('Chandan')
# print(mylist)

# mylist.extend(['chandan'])        # square bracket
# print(mylist)

# mylist.extend('chandan')        # string is also itrable
# print(mylist)


# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(list1[::-1])        # for reverse the list
# print(list1[-1:-10:-1])
# print(list1[-1:-len(list1)-1:-1]) # for reverse the list



# Replace the first three element of the list
list1 = [1,2,3,4,5,6,7,8,9,10]
list1[0:3] = [10,20,30]
print(list1)

list1[0:3] = [10,20,30,40,35]
print(list1)


list2 = [1,2,3,4,5]
a = list1 + list2   # create new list
print(a)

new_list = list1 + [3]
print(new_list)            # Modify the same list

new_list = list1.extend([26,46,8436])
print(list1)               # Modify the same list


newlist = list1 *3           # Create a new list
print(newlist)


print( 6 in list1)
print( 6 not in list1)


for x in list1:
    print(x)

for i in range(len(list1)):
    print(list1[i])

for i in range(-1,-len(list1)-1,-1):
    print(list1[i])

i = 0
while i < len(list1):
    
    print(list1[i])
    i+=1

list1[len(list1):] = [10,20,30]  # insert the multiple element in end
print(list1)



# # insert can also done by indexing method
list1[4:4] = [30]
print(list1)

l2 = list1.copy()
print(l2)



# Index
L1 = [1,2,3,6,4,5,6,10]
print(L1.index(10))
print(L1.index(6,4))
print(L1.index(6,4,7))

print(L1.count(6))
(L1.reverse())
print(L1)

L1.sort()
print(L1)

L1.sort(reverse=True)
print(L1)



l2 = ['yy','jj','mm','BB','aa','ZZ']
l2.sort()
print(l2)

l2.sort(key = str.lower)  # considered all as lower case 
print(l2)
l2.sort(key = str.upper,reverse = True)  # considered all as lower case 
print(l2)

print(sorted(l2)) # Directly gives the sorted reverse list



#List comprehentions
l1 = []
for x in range(10):   # Method 1
    l1.append(x)
print(l1)


# l1 = [x**2 for x in range(1,6)]  # method 2
# print(l1)

# l3 = [x for x in (10,5,7,8,12,3) if x%2==0]
# print(l3)

# l4 = [x.lower() for x in 'Python']
# print(l4)

# l3 = [x for x in 'ab12de-&fg4$hi2' if x.isalpha()]
# print(l3)

# name = input("Enter the name:")   # method 1
# l6 =  name.split()
# print(name)

# name = input("Enter the name:").split()] # method 2
# print(name)



#Nested List

list = [10,20,['a','b',['c','d']],30,40]
print(list[0])
print(list[2][1])
print(list[2][2][1])



# With the help of nested list we can prepared matric

A = [[1,2,3],[4,5,6],[7,8,9,]]
# A.sort(reverse=True)
# [A[0].sort(reverse = True),A[1].sort(reverse = True),A[2].sort(reverse = True)] 
# print(A)
B =[[9,8,7],[6,5,4],[3,2,1]]
C = []                               # Sum of two matrics
for i in range(len(A)):
    S = []
    for j in range(len(A[0])):
        # print(i,j)  # for cheaking
        S.append(A[i][j]+B[i][j])
    print(S)
    break
    C.append(S)
print(C)






 