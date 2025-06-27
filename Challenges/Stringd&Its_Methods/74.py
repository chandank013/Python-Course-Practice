# Rearranfe : lowercase then uppercase

upper_1  = input("Enter the string:")

lower = ''
upper = ''

for x in upper_1:
       
    if x.islower():
        
        lower += x
    
    else:
        upper += x

str_2 = lower + upper
print(str_2)



# Remove punctuation

punctuations = '''!(-[]{};:'"\,<>./?@#$%^&*_~'''

s2 = '[my_python@gmail.com]'


s1 = ''
for i in s2:
    if i not in punctuations:
        s1 += i
print(s1)
        