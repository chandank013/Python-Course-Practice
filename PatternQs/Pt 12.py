# Diamond Patterns
#11 Diamond of stars

n = 5
for i in range(n):
    print(" " * (n-i) + "*" * (2*i - 1))
n = 5
for i in range(n,0,-1):
    print(" " * (n-i) + "*" * (2*i - 1))