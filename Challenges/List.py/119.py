 # Transpose of a matrix:

list_1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4],]

list_2 = []
 
# for i in range(4):
#     s = []
#     for j in range(3):
#         # print(i,j)            for cheaking
#         s.append(list_1[j][i])
#     list_2.append(s)
# print(list_2)

for i in range(len(list_1[0])):
    s = []
    for j in range(len(list_1)):
        # print(i,j)            for cheaking
        s.append(list_1[j][i])
    list_2.append(s)
print(list_2)