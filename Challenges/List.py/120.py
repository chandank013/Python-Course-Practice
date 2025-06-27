 # Finding the words starting with the given letter in the list.

letter = input("Enter the word:")
food = ['pizza','nuggets','hotdog','noodles','pasta','burger']

for x in food:
    if x.startswith(letter):
        print(x)



