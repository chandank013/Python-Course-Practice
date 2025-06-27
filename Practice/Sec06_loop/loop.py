                            # Loops

range(5)


## for loop
for i in range(5):
    print(i)


for i in range(1,6):
    print(i)


for i in range(1,10,2):
    print(i)


for i in range(10,1,-1):
    print(i)


for i in range(10,1,-2):
    print(i)


## strings

str="Chandan Kumar"

for i in str:
    print(i)


## while loop

## The while loop continues to execute as long as the condition is True.
count=0

while count<5:
    print(count)
    count=count+1


## Loop Control Statements

## break
## The break statement exits the loop permaturely

## break sstatement

for i in range(10):
    if i==5:
        break
    print(i)
   

## continue

## The continue statement skips the current iteration and continues with the next.

for i in range(10):
    if i%2==0:
        continue
    print(i)


## pass
## The pass statement is a null operation; it does nothing.

for i in range(5):
    if i==3:
        pass
    print(i)


## Nested loopss
## a loop inside a loop

for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")


## Examples- Calculate the sum of first N natural numbers using a while and for loop

## while loop  

n=10   
sum=0
count=1

while count<=n:
    sum=sum+count
    count=count+1

print("Sum of first 10 natural number:",sum)


n=10   
sum=0
for i in range(11):
    sum=sum+i

print(sum)


## Example- Prime numbers between 1 and 100

for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)



