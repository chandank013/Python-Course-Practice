# Cheak if a student has passed or failed , by taking marks in three subject.

math = int(input(" Enter the marks of math: "))
physics = int(input(" Enter the marks of physics: "))
chemistry = int(input(" Enter the marks of chemistry: "))

if (math >= 45) and (physics >= 45) and(chemistry >= 45):
    print('Student Passed')
else:
    print('Student Failed')


# Cheak the given lower case character is a vowel or constant.

str_lower_case = input(" Enter the lower case latter:")

if str_lower_case == ('a' or 'e' or 'i' or 'o' or 'u'):
    print("vowel")
else:
    print("constant.")



# Check the grade of the student based on average marks.

average_marks = (math + physics + chemistry) / 3

if average_marks >= 90:
        print("Grade: A")
elif average_marks >= 75:
        print("Grade: B")
elif average_marks >= 50:
        print("Grade: C")
else:
        print("Grade: F")



 # Check eligibility for voting.

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
