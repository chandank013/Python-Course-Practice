# Concatanate all integer from a list in to single number.

l1 = [4,5,2,12,35,32]

sum = ''

for x in l1:
    sum += str(x)


print(int(sum))