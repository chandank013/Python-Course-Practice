# Maximum index sum of two lists

fev1 = ['pizza', 'nugget', 'hotdog','noodles','pasta','burger']
fev2 = ['burger', 'hotdog','noodles','pasta','nugget','pizza']

index1 = 10
index2 = 10
for i in range(len(fev1)):
    indx = fev2.index(fev1[i])

    if i + indx < index1 + index2:
        index1 = i
        index2 = indx

print(fev1[index1],index1+index2)



