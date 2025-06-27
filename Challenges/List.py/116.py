# Find the number of occurences of each item.
list_1 = ['A','B','C','D','E','A','B','E','B','D','B','E']

result = []
for x in list_1:
    if x  not in result:
        result.append(x)
        count = list_1.count(x)
        result.append(count)
print(result)

