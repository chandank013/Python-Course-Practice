
n = 6
for i in range(n+1):
    for j in range(n):
        if i == j or i+j == n-1:
            print("*" , end= " ")
        else:
            print(" ", end=" ")
    print()

