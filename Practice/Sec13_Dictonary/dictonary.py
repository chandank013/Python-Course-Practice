                        # Dictonary

# dict1 = {
#     'abscus': 'a calculator',
#     'bachelor': 'unmarried person',
#     'cable': 'strong rope',
# }

# dict2 = {
#     101:'John',
#     102:'smith',
#     103:'chandan',
#     104:'david',
# }
# dict2[103] = 'Methew'
# print(dict2[103])
# for i in dict2:
#     print(i)

# for i in dict2:
#     print(i,dict2[i])

# dict1 = dict()
# print(type(dict1))

# for x in range(1,6):               # Inserting element using for loop
#     dict1[x] = x**2
# print(dict1)

# dict4 = dict(((1,2),(2,3),(3,6)))
# print(dict4)
# dict4 = dict(('ab','cd','ef'))
# print(dict4)



l1 = ['A','B','C']              # Enumarate mean giving numbering to item in variable    
# for item in enumerate(l1):
#     print(item)

# dict4 = dict(enumerate(l1))
# print(dict4)

# dict5 = {x:x**2 for x in range(1,6)}
# print(dict5)


# dict5 = dict((x,x**2) for x in range(1,6))
# print(dict5)



# # working of zip
# l1 = [1,2,3,4,5]
# l2 = ['Chandan','Nitish','Piyush','Dharmik',]

# for x,y in zip(l1,l2):
#     print(x,y)

# # for x,y in enumerate(l1):
# #     print(x,y)
# # dict8 = {x:y for x,y in enumerate(l1)}
# dict8 = dict((x,y) for x,y in enumerate(l1))
# print(dict8)



dict2 = {
    101:'John',
    102:'smith',
    103:'chandan',
    104:'david',
}
# for i in dict2:
#     print(i,dict2[i])                # method 1
#     print(i,dict2.get(i))            # method 2

# print(dict2.keys())
# print(dict2.values())
# print(dict2.items())

# for i in dict2.keys():
#     print(i,dict2[i])    

# for i in dict2.values():
#     print(i)   

# for i in dict2.items():
#     print(i)    
 


# Dictonary method

# dict = dict2.copy()
# print(dict)
# print(id(dict2[103]))    # .copy() provide the valeue of same id in another diconary
# print(id(dict[103]))

# dict3 = {
#     105:'polishing',
#     106:'casting',
#    }
# dict2.update(dict3)
# print(dict2)


print(dict2.popitem())

