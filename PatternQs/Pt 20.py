# Alphabet Patterns
# Triangle of alphabets
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()



n = 5
for i in range(1, n + 1):
    print(" "*(n-i),end=" ")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()