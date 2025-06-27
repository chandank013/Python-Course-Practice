                    # Regular Expression

from re import*

match('a','a').group()
match('a|b','a').group()
match('a|b','b').group()
match('abc','abcd').group()
match('[abc]','abcd').group()
match('[abc]','bcd').group()
match('[abc]+','cccc').group()
match('[abc]+','ababcbbaba').group()
match('[abc]+','ababcaccbba').group()
match('[abc]{5}','ababcaccbba').group()


match('[a-z]+','abcdef').group()
match('[a-z]+','python').group()
# match('[^a-z]+','abcdef').group()
match('[^a-z]','A-23+@').group()
match('([a-z]+)|([A-Z]+)','abc').group()
match('([a-z]+)|([A-Z]+)','abcD').group()


# x = r'^Hell'
# c = compile(x)
# r = c.search('Hello world')
# r.group()

# p = r'rld$'
# c = compile(p)
# r = c.search('Hello world')
# r.group()

# import re
# str = 'bob.com'
# match = re.search(r'[\w.-]+@[\w.-]+', str)
# if match:
#     print(match.group())
# else :
#     print('the email is not valid')

