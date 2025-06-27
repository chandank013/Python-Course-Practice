# A dding of two matrices

l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l2 = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]

s = []

# for i in range(3):
#     c = []
#     for j in range(4):
#         add = l1[i][j] + l2[i][j]
#         c.append(add)
#     s.append(c)
# print(s)

for i in range(len(l1)):
    c = []
    for j in range(len(l1[0])):
        add = l1[i][j] + l2[i][j]
        c.append(add)
    s.append(c)
print(s)