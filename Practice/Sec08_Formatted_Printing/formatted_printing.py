                        # Formatted Printing

# s = 'A'
# print(ord(s))
# print(chr65)

# s ='\u03b1'
# print(s)


# Unicode
# my_name = '\u091a\u0902\u0926\u0928  \u0915\u0941\u092E\u093E\u0931'
# print(my_name)
# name_1  = '\u0928\u093F\u0924\u0940\u0936  \u0928\u0935\u0940\u0928'
# print(name_1)

# print('abcdefghi', end ="")
# print('def')

# print('abcd\nefghi', end ="")
# print('def')


# print('abcd\fefghi', end ="")
# # print('def')


# print('abcd\refghi', end ="")
# print('def')

# print('abcde\bfghi',end = '')
# print('def')

# print('abcde\vfghi',end = '')
# print('def')

# print('abcde\tfghi',end = '')
# print('abcde\afghi',end = '')

# print('\t\t\t\tWelcome')
# print('\t\tJemes')
# print('\t\tJohn\n\t\tsmith')


# print('john's') # It show error
# print('john\'s')

# print("john\"s")
# print('abcg\\ndghs')  # If we take double slaces then '\n' would not work

# print(r'abcg\\ndghs')
# print(r'abcg\ndghs')

# print('\N{pound sign}')
# print('\N{dollar sign}')
# print('\N{rupee sign}')
# print('\N{yen sign}')
# print('\N{copyright sign}')
# print('\N{latin small letter a}')
# print('\N{superscript five}')
# print('\N{subscript five}')



# print('Hello','World')
# print('Hello'+'World')
a = "ram"
b = 'shyam'
c = "sundar"
# print(a,b,c,sep = '-')

# print(a, end = '\t')
# print(b, end = '\t')
# print(c)

# print(a, end = '\n')
# print(b, end = '\n')
# print(c)

# print(a, end = ' ')
# print(b, end = ' ')
# print(c)



# # C Styte Printing
# roll_no = 10
# name = 'Ravi'
# avg = 8.7395626

# print('Student name is %s, his roll_no is %f and average is %f'%(name ,roll_no,avg))
# print('Student name is %10s'%name)
# print('Student name is %-8s and'%name)
# print('%2.3f'%avg)



# Frmatted Printing

a = 22
b = 7
c = a/b

# print('Divosion of {0} and {1} is {2}'.format(a,b,c)) # Even we do not give index then it automatically take whole number as counting
# print('Divosion of {} and {} is {}'.format(a,b,c))
# print('Divosion of {2} and {1} is {0}'.format(a,b,c))
# print('Divosion of {2} and {1} is {0}'.format(c,b,a))
# print('Divosion of {0:10} and {1:8} is {2:2.1}'.format(a,b,c))


# Use for allignment
# print('Divosion of {0:<10} and {1:^15} is {2:2.4}'.format(a,b,c))
# x = 37568276848
# print('{0:20,}'.format(x))



# Conversion
# print('Divosion of {0:<10} and {1:^15} is {2:E}'.format(a,b,c))
# print('Divosion of {0:<10} and {1:^15} is {2:F}'.format(a,b,c))
print('Divosion of {0:<10} and {1:^15} is {2:f}'.format(a,b,c))
# New style in python
print(f'Divosion of {a:<10} and {b:^15} is {c:2.5}')



