                        # Tuple

tuple = ('Jack',45,38.6,False,5+4j,'Jill',45)

t1 = ()
t2 = (1,)
print(t2)
print(type(t1))
print(tuple[2])


T4 = tuple((1,2,3,4,5))   # Double parenthisis is necessary same as list
print(type(T4))

T4 = tuple([1,2,3,4,5])
print(type(T4))


tup = tuple(('python'))
print(tup)
print(type(tup))



# Packing
t34 = 10,100,20,30,40          # Automatically pack them as a tuple
print(type(t34))
print(t34)



# Unpacking can be done for string tuple and list but packing will happen only with tuple
a,b,c = 'SKY'
a,b,c = [1,2,3]
a,b,c = (1,2,3)
print(a)



# to unpack more number of value in less number of variable like this
t = 10,20,30,40,50
a,b,*c=t
print(a)
a,*b,c = t
print((b))


l1 = [x for x in range(10)]  # it work in list
print(l1)

t1 = (x for x in range(10))     # it does not work directly work in  tuple
print(t1)

t2 = tuple(x for x in range (10))   # Now it work in tuple
print(t2)

t3 = (*(x for x in range(1,11,2)),)     # At place of tuple we can use * for creating tuple fron user
print(t3) 

t4 = (*(x for x in 'Python'),)
print(t4)

t5 = (*(x for x in 'PyThOn' if x.islower()),)
print(t5)

t5 = (tuple(x for x in 'PyThOn' if x.islower()))
print(t5)

t6 = (tuple(x**2 for x in (1,2,3,4,5) ))
print(t6)

t8 = (2,3,3,4,6,4,4,6,7,5,4,3,35,3,6,4,3,3)
print(t8.count(t8[1]))
print(t8.index(3,3,12))



tuple = ('Jack',45,38.6,False,5+4j,'Jill',45)
for i in tuple:
    print(i,end = ' ')



tuple = ('Jack',45,38.6,False,5+4j,'Jill',45)

for i in range(len(tuple)):
    print(tuple[i])

i= 0
while i<len(tuple):
    print(tuple[i])
    i+=1

print(tuple[4])
print(tuple[-1])
print(tuple[:])
print(tuple[4:len(tuple)])
print(tuple[-1:-len(tuple)-1:-1])



tup1 = (1,2,3)
tup2 = (4,2,5)
print(tup1+tup2)
print(tup1+tuple([7,6,8]))
print(5 in tup1)
print(5  not in tup1)
