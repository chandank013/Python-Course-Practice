list_1 = [10,15,6,9,12,8,4]      # Method 1
list_2 = [14,6,19,4,7,10,11]

list_3 = []
for x in list_1 and list_2:
    if x  in list_1 and list_2:
        list_3.append(x)
print(list_3)



for x in list_1:                 # Method 2
    if x in list_2:
        list_3.append(x)
print(list_3)