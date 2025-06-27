#03 Pattern of zero

n = 5
for i in range(n):
    for j in range(n):
    #     print('(',i,j,')', end=" ")    # only for understanding
    # print()
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()