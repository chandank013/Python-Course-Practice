                        # String

s_1 = 'Hello moto'
s2 =len(s_1)
print(s2)



for x in s_1:
    for j in s_1:
       if x>j:

          print(s_1,end=(' '))
    print('')

for x in s_1:
    print(x)

s6 = 'How'+' are'+' you'
print(s6)

for i in range(0,len(s_1)):
             print(s_1[i])

for i in range(0,len(s_1)):
    print(s_1[i])
       
       
for i in range(0,len(s_1)):
    print(s_1[i],end="")

for i in range(len(s_1,)-1,-1,-1):
    print(s_1[i],end="")


for i in range(len(s_1)-1,-1,-1):
    print(s_1[i])

print(s_1[0:len(s_1):1])
print(s_1[:len(s_1):1])
print(s_1[::])

print(s_1[-1:-len(s_1)-1:-1])
print(s_1[-1:-len(s_1)-1:-1])



s1 = 'abcde'
s2 = 'abcdf'
c= s1>s2
print(c)

s1 = 'Abcdef'
s2 = 'abcdef'

c= s1==s2
print(c)

s = 'hello, how are you'
print(type(s))
dir(int)
help(s.endswith) # to cheak the work of particular method



for x in s:   # For counting a particular word in given string
   x=s.count('o')
print(x)

x= s.find('o',5,15)
print(x)

s1 = 'python'
# print(s1.rjust(20))
print(s1.rjust(20,'*'))

s2 = '....  ... ++aaapython'
print(s2.lstrip('.'))

s2 = 'HELLO'
s3 = 'hello'
# print(s2==s3)
print(s2.lower()==s3.lower())

s1 = 'Bu\u00DF'
print(s1)
s2 = 'Buss'
# print(s1 == s2)
# print(s1.lower() == s2.lower())
print(s1.casefold() == s2.casefold())

s1 = '\u01C6'
print(s1)
print(s1.upper())

l1 = ['john','smith','ajay']
s1 = '-'
print(s1.join(l1))

l1 = 'Chandan is a new emersing coder from iiit dharwad'
print(l1.split())   # it form string to list from sentances

l1 = 'Chandan is a- new emersing coder- from iiit dharwad'
print(l1.split('-'))   # it form string to list from sentances




