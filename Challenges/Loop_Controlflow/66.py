# WAP to use nested loop


# for i in range(0,5):
#     for j in range(0,5):
#         print('(',i+j,')', end=" ")
#     print("")


# for i in range(0,5):
#     for j in range(0,5):
#         print('*', end=" ")
#     print("")


# for i in range(0,5):
#     for j in range(0,5):
#         if i<j:
#            print('*', end=" ")
#     print("")

# for i in range(0,5):
#     for j in range(0,5):
#         if i>j:
#            print('*', end=" ")
#     print("")


# s1 = 'abc'
# s2 = 'xyz'
# for i in s1:
#     for j in s2:
#         print(i,j, end=" ")
#     print('')

for i in range(0,5):
    for j in range(0,5):
        for k in range(0,5):
            if i>j==k:
               print('*', end=" ")
            print("")


