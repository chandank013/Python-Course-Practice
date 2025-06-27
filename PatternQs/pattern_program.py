
# Advanced Patterns

# Zig-Zag Pattern
n = 5
for i in range(1, 4):
    for j in range(1, n + 1):
        if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Advanced Number Patterns
# Pyramid with Increasing Numbers
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     num = 1
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

# Diamond with Numbers
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end="")
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print()
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end="")
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print()

# Pyramid with Continuous Numbers
# n = 5
# num = 1
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

# Square with Increasing Numbers
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end=" ")
#     print()

# Snake Pattern of Numbers
# n = 5
# num = 1
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(num, end=" ")
#         num += 1
#     print()

# Alphabet Patterns
# Full Alphabet Triangle
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()

# Reverse Alphabet Triangle
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(i):
#         print(chr(65 + i - j - 1), end=" ")
#     print()

# Diamond with Alphabets
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(i):
#         print(chr(65 + j), end="")
#     for j in range(i - 2, -1, -1):
#         print(chr(65 + j), end="")
#     print()
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     for j in range(i):
#         print(chr(65 + j), end="")
#     for j in range(i - 2, -1, -1):
#         print(chr(65 + j), end="")
#     print()

# Right Triangle of Alphabets
# n = 5
# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(65 + i - 1), end=" ")
#     print()

# Zigzag Alphabet Pattern
# n = 7
# for i in range(1, 4):
#     for j in range(1, n + 1):
#         if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
#             print(chr(65 + (i + j - 1) % 26), end="")
#         else:
#             print(" ", end="")
#     print()

# Alphabet and Star Mixed Patterns
# Hollow Diamond with Alphabets
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print(chr(64 + i), end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print(chr(64 + i), end="")
#         else:
#             print(" ", end="")
#     print()

# Alphabet Pyramid
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(chr(64 + j), end=" ")
#     print()

# Reverse Alphabet Pyramid
# n = 5
# for i in range(n, 0, -1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(chr(64 + j), end=" ")
#     print()

# Alternating Alphabets and Stars
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print("*", end=" ")
#         else:
#             print(chr(64 + i), end=" ")
#     print()

# Geometric and Grid Patterns
# Square Grid with Alternating Stars and Spaces
# n = 5
# for i in range(n):
#     for j in range(n):
#         if (i + j) % 2 == 0:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Triangle Grid with Alphabets
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(chr(64 + i), end=" ")
#     print()

# Hollow Square Pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Hollow Right Triangle
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Triangle with Increasing Numbers
# n = 5
# num = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     print()


# Number Patterns
# Diamond of Numbers
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Pascal’s Triangle
# n = 5
# for i in range(n):
#     print(" " * (n - i), end="")
#     num = 1
#     for j in range(i + 1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)
#     print()

# Half Pyramid of Consecutive Numbers
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Reverse Pyramid of Numbers
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Number Grid
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(j, end=" ")
#     print()


# Special and Creative Patterns
# Heart Pattern
# for row in range(6):
#     for col in range(7):
#         if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# Butterfly Pattern
# n = 5
# for i in range(1, n + 1):
#     print("*" * i + " " * (2 * (n - i)) + "*" * i)
# for i in range(n - 1, 0, -1):
#     print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Wave Pattern
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" + " " * (2 * (i - 1)) + ("*" if i > 1 else ""))
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" + " " * (2 * (i - 1)) + ("*" if i > 1 else ""))

# Checkerboard Pattern
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if (i + j) % 2 == 0:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()







# Hollow Diamond Inside a Square
# n = 7
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i + j == n // 2 + 2 or j - i == n // 2 or i - j == n // 2 or i + j == (n + n // 2 + 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# # Hourglass of Numbers
# n = 5
# for i in range(n, 0, -1):
#     print(" " * (n - i), end="")
#     for j in range(1, 2 * i):
#         print(j, end="")
#     print()
# for i in range(2, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, 2 * i):
#         print(j, end="")
#     print()
# Floyd's Triangle
# n = 5
# num = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     print()
# Zigzag Number Pattern
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if (i + j) % 2 == 0:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()
# Spiral Number Pattern
# n = 4
# m = 2 * n
# matrix = [[0] * m for _ in range(m)]
# num = 1
# for i in range(n):
#     for j in range(i, m - i):
#         matrix[i][j] = num
#         num += 1
#     for j in range(i + 1, m - i):
#         matrix[j][m - i - 1] = num
#         num += 1
#     for j in range(m - i - 2, i - 1, -1):
#         matrix[m - i - 1][j] = num
#         num += 1
#     for j in range(m - i - 2, i, -1):
#         matrix[j][i] = num
#         num += 1
# for row in matrix:
#     print(" ".join(f"{x:2}" for x in row))
# Mixed Patterns with Alphabets and Numbers
# Alphabet and Number Triangle
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print(chr(64 + j), end=" ")
#         else:
#             print(j, end=" ")
#     print()
# Diamond with Alternating Numbers and Stars
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end="*")
#     print()
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end="*")
#     print()
# Alphabet Pyramid with Spaces
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(chr(64 + j), end=" ")
#     print()
# Creative and Fun Patterns
# Wave of Stars
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("*" + " " * (2 * (i - 1)) + ("*" if i > 1 else ""))
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     print("*" + " " * (2 * (i - 1)) + ("*" if i > 1 else ""))
# Hollow Butterfly
# n = 5
# for i in range(1, n + 1):
#     print("*" + " " * (i - 1) + "*" + " " * (2 * (n - i)) + "*" + " " * (i - 1) + "*")
# for i in range(n - 1, 0, -1):
#     print("*" + " " * (i - 1) + "*" + " " * (2 * (n - i)) + "*" + " " * (i - 1) + "*")
# Star Flower
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)
# Number and Spiral Mix
# Square Spiral Numbers
# n = 4
# size = n * 2 - 1
# matrix = [[0 for _ in range(size)] for _ in range(size)]
# num = 1
# for layer in range(n):
#     for i in range(layer, size - layer):
#         matrix[layer][i] = num
#         num += 1
#     for i in range(layer + 1, size - layer):
#         matrix[i][size - layer - 1] = num
#         num += 1
#     for i in range(size - layer - 2, layer - 1, -1):
#         matrix[size - layer - 1][i] = num
#         num += 1
#     for i in range(size - layer - 2, layer, -1):
#         matrix[i][layer] = num
#         num += 1
# for row in matrix:
#     print(" ".join(f"{x:2}" for x in row))
# Star and Number Checkerboard
# n = 5
# for i in range(n):
#     for j in range(n):
#         if (i + j) % 2 == 0:
#             print("*", end=" ")
#         else:
#             print(i + 1, end=" ")
#     print()





# Complex Star and Number Patterns
# Circle Pattern
# n = 6
# for i in range(n * 2):
#     for j in range(n * 2):
#         if (i - n) ** 2 + (j - n) ** 2 <= n ** 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# Sine Wave Pattern
# n = 5
# for i in range(n):
#     for j in range(10):
#         if int(j % (2 * n) / n) == 0:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# Diamond of Numbers
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# Combination Patterns
# Star and Number Combination (Pyramid)
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print(j, end=" ")
#         else:
#             print("*", end=" ")
#     print()
# Number Tree
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# Reverse Pyramid of Stars and Numbers
# n = 5
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print(j, end=" ")
#         else:
#             print("*", end=" ")
#     print()
# Star Spiral
# n = 5
# for i in range(1, n + 1):
#     print("* " * i)
# for i in range(n - 1, 0, -1):
#     print("* " * i)
# Geometric Star Patterns
# Inverted Right Triangle of Stars
# n = 5
# for i in range(n, 0, -1):
#     print("* " * i)
# Full Diamond with Stars
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)
# Hollow Full Diamond of Stars
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, 2 * n):
#         if j == n - i + 1 or j == n + i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(1, 2 * n):
#         if j == n - i + 1 or j == n + i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# Complex Number Patterns
# Square Pattern of Increasing Numbers
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end=" ")
#     print()
# Left-Aligned Right Triangle of Numbers
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# Right-Aligned Triangle of Numbers
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()