                    # Data Structure Module

#Counter:

l = ['Mark','Jonny','David','Mark','Jonny','Mark','James','Methew']  
from collections import Counter

c = Counter(l)
print(c)
print(c['Mark'])
print(c.get('Mark'))
print(c.keys())
print(c.values())

print(c.update({'Ajay':4}))
print(c)

print(c.elements())
for i in c.elements():
    print(i)

c.pop('Ajay')  # Delete 'Ajay'
print(c)


c.update({'Ajay':4})
print(c.most_common(1))   # it give most popular item
print(c.most_common(2))   # it give two most popular item



# Deque:
from collections import deque
L = [1,2,3,4,5]

q = deque(L)
print(q)

q.append(6)
print(q)

q.appendleft(7)
print(q)

q.pop()
print(q)

q.popleft()
print(q)

q.extend([10,20,30])
print(q)

q.extendleft([10,20,30])
print(q)

q.rotate(3)
print(q)



# Array:

import array
ar2 =array.array('i',[10,20,30,40])
print(ar2)

s1 = b'abcdefg'
ar2 = array.array('b',s1)
print(ar2)
print(ar2[0])
ar2.append(104)
print(ar2)
print(ar2.index(102))
print(ar2.typecode)
print(ar2.typecode)



# Heapq:
import heapq

H = []
heapq.heappush(H,20)    # Value is not inserting according to as i want put in the list rearrange itself
heapq.heappush(H,50)
heapq.heappush(H,10)
heapq.heappush(H,40)
heapq.heappush(H,30)
heapq.heappush(H,60)
print(H)
heapq.heappop(H)        # After each deleting list rearrange itself according to the heap data structure and keep smallar value at beggenning 
print(H)
heapq.heappop(H)
print(H)

l = [50,30,60,40,70,20,10]
heapq.heapify(l)       # it convert given list in the form of heap.
print(l)
print(heapq.nlargest(2,l))
print(heapq.nsmallest(2,l))



# Bisect:  # It mentain the list in sorted order
import bisect
l = [10,20,20,30,40,50,60,70,90]

bisect.insort(l,25)
print(l)
bisect.insort_left(l,90)
print(l)
print(id(l[9]))
print(id(l[10]))


print(bisect.bisect(l,5))      # not insered only give the posotion
print(bisect.bisect_left(l,20))      # not insered only give the posotion
    
print(bisect.bisect_right(l,25))  



#Copy:
# copy.copy()
import copy

l =[10,20,30,40,50]
l1 = copy.copy(l)
print(l1)
print(id(l))    # Both having different id's
print(id(l1))



# copy.deepcopy()
import copy
class Person:
    def __init__(self,name):
        self.name = name

l = [Person('John'),Person('Prem'),Person('Ravi'),Person('Chandan')]
l1 = copy.deepcopy(l)
print(l1)

print(id(l))   # Both list have different id's
print(id(l1))

print(id(l[0]))   #Both element of list  have different id's
print(id(l1[0]))
        

