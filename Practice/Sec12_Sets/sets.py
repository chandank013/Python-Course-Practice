                            # Set

s1 = {1,2,3,4,'jack',3.4,'Jack'}
print(type(s1))

s2 = set(1,2,3,4)       # Not a repersentation of set
print(type(s2))

s6 = set((1,2,3,4))       # repersentation of set
print(type(s6))

s3 = set('Python')       # Becouse no indexing
print(s3)

s4 = {10,20,40,50,86}
print(s4)
s4.discard(50)
s4.add(100)
print(s4)



set1 = {1,2,3,4,5,7}
set2 = {5,7,9,10,11}
print(set1.intersection(set2))
print(set2.intersection_update(set1))


print(dir(set))

# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__',
# '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
# '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']



s = set()                # method 1
for x in range(1,11):
    s.add(x)
print(s)


s1 = {x for x in range(10)}
print(s1)

s2 = {x**2 for x in [2,3,4,5,6]}
print(s2)

s3 = {x for x in (10,5,7,8,12) if x%2 == 0}
print(s3)

s4 = {x for x in 'philippines'}
print(s4)