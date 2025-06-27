
# To cheak read mode
# file = open('Mydata.txt', 'r')
# str1 = file.read(5)
# print(str1)
# print(type(str1))

# str1 = file.read(5)
# print(str1)
# str1 = file.read(48)
# print(str1)

# # To cheak write mode
# file = open('Modedemo.txt', 'w')
# file.write('Hello\n')
# file.write('How are you?\n')
# file.close()


# # To cheak write mode
# file = open('Modedemo.txt', 'a')
# file.write('I am learning python\n')
# file.write('It is very easy language\n')
# file.write('I am precticing\n')
# file.close()


# # To cheak write and read mode
# file = open('Mydata.txt', 'r+')
# str1 = file.read(10)
# print(str1)
# file.write('good bye\n')
# file.close()


# # Operations on file
# file = open('text.txt', 'w')
# print(file.name)
# print(file.mode)
# print(type(file))
# print(dir(file))
# print(file.closed)

# 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']


# # Operations on file i.e readline
# file = open('text.txt', 'r')

# line = file.readline()
# print(line)

# line = file.readline()
# print(line)
# print(file.closed)


# # Operations on file i.e readlines
# file = open('text.txt', 'r')

# lines = file.readlines()    # it convert the line in the element of the list so we can excess all the line by using for loop.
# for line in lines:
#     print(line, end = '')



# Operations on file i.e write(str)
# file = open('text.txt', 'w')
# str1 = 'Python is simple\nit is easy\nevery thing is an object'
# file.write(str1)


# Operations on file i.e writelines(str)
# file = open('text.txt', 'w')
# list1 = ['Python is simple\n','it is easy\n','every thing is an object']
# file.writelines(list1)



