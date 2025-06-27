# Cheaking two string are anagram.

ana_1 = input("Enter the str_1:")
ana_2 = input("Enter the str_2:")

l = sorted(ana_1)
b = sorted(ana_2)

if l == b:
    print("The given string is anagram.")
else:
     print("The given string is not anagram.")


# On the basis of length
if len(ana_1) != len(ana_2):
    print("Not anagram")
else:
    for i in len(ana_1):
        if i not in ana_2:
            print("Not anagram")
            break

    else:
        print("Anagram")
