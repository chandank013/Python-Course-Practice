# Method 01
# Cheaking and Removing if there are any  dublicates in a list.

list_1 = input("Enter the elements of the list from keyboard:").split()
list_2 = []
for x in list_1:
    if x not in list_2 :
        list_2.append(x)
print(list_2)


# Method 02
# Define the list with duplicates
original_list = [1, 2, 2, 3, 4, 4, 5, 1]

# Iterate through the list in reverse order to avoid skipping elements
for i in range(len(original_list) - 1, -1, -1):
    if original_list[i] in original_list[:i]:  # Check if the element appears earlier in the list
        original_list.pop(i)  # Remove the duplicate

# Print the result
print("List after removing duplicates:", original_list)
 
 
       




