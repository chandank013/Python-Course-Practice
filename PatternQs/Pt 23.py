#23 Diamond of alphbet




n = 5
for i in range( 0,n+1):
    print(" "*(n-i),end=" ")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


n = 5
for i in range(n-1, 0, -1):
    print(" " * (n-i),end=" ")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()






    # Diamond of alphabets
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(65 + j), end="")
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(65 + j), end="")
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")
    print()
