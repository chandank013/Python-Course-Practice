 # Hourglass pattern

n = 5
for i in range(n,0,-1):
    print(" " * (n-i), end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(2,n+1):
    print(" " * (n-i), end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
