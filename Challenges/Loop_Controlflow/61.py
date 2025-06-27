# febonacci series

a = 0
b = 1
c = int(input("Enter the number of terms:"))

for i in range(c):
    print(a)
    c = a + b
    a = b
    b = c


