#09 Half pyramid of numbers

n = 5
for i in range(n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n = 5
for i in range(n+1,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()