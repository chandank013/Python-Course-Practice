
# Inverted pyramid of numbers
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()



n = 5
for i in range(n,0,-1):
    print(" " * (n - i), end=" ")
    for j in range(1,i + 1):
        print(j, end=" ")
    print()