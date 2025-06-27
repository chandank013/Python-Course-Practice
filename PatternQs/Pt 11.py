#11 Floyd's triangle

n = 5
num = 1
for i in range(n+1):
    for j in range(i):
        print(num , end = " ")
        num+=1
    print()

