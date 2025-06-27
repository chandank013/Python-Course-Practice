# Random

# Program for finding binary number
num_1 = int(input("Enter the number:"))

bin = 0

while num_1 > 0:
    r = num_1 % 2
    print(r)
    num_1 = num_1 // 2
    print(num_1)
    bin = bin * 10 + r
    print(bin)

rev = 0   # for reversing the binary number
while bin > 0:
        p = bin % 10
        bin = bin // 10
        rev = rev * 10 + p

        print(rev)

   
# WAp to print table using for loop.

num_1 = int(input("Enter the number to get table:"))

for i in range(1, 11):
    print(num_1,'X',i,'=',num_1*i)


#  WAP to print terms of AP.

a = int(input("Enter the First term of AP:"))
d = int(input("Enter the common difference of AP:"))
n = int(input("Enter the  number of terms have to print:"))

p = a+(n-1)*d
for i in range(a,p,d):

    print(i)



