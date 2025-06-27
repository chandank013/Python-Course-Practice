# Hollow diamond pattern

n = 5
for i in range(1,n+1):
    print(" " * (n-i) + "*" +" " * (2 * i - 3) + ("*" if i > 1 else " "))
for i in range(n-1,0,-1):
    print(" " * (n-i) + "*" +" " * (2 * i - 3) + ("*" if i > 1 else " "))
    


# Diamond with Borders
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2*i):
        # print(i,j, end=" ")     # Only for understanding
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()