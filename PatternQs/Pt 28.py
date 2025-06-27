# Hollow inverted pyramid

n = 5
for i in range(n,0,-1):
    print(" "*(n-i), end=" ")
    for j in range(1,i +1):
        if j == 1 or i == j or i == n:
            print("*", end=" ")
        else:
            print(" " , end= " ")
    print()
