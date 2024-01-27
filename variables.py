x = 5
y = "John"
print(x)
print(y)

x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

x = "John"
# is the same as
x = "John"


a = 4
A = "Sally"
# A will not overwrite a

# len function
course_name = "Python Programming"
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[1])
print(course_name[0:3])
print(course_name[0:4])

print(course_name[:3])

# Escape Sequences
# \"
# \'
# \\
# \n

print('Python "Programming')
print("Python 'Programming")
print("Python \\Programming")
print("Python \nProgramming")


# Formatted Strings
first = "Ahmed"
last = "Ziaus Salam"
full = first + "" + last
print(full)

first = "Ahmed"
last = "Ziaus Salam"
full = f"{first} {last}"
print(full)

first = "Ahmed"
last = "Ziaus Salam"
full = f"{len(first)} {2+2}"
print(full)

# strings method
course = "Python Programming"
print(course.upper())
print(course)

course = " python programming"
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("mamun" not in course)

# Numbers
x = 1  # integer
x = 1.1  # floats
x = 1 + 2j  # a + bi #complex number

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 5)
print(10 % 5)  # modulus
print(10**3)

x = 10
x += 3  # Augmented Assignment Operator
print(x)

# working with numbers
print(round(2.9))
print(abs(-2.9))

import math  # math module

print(math.ceil(2.2))
print(math.asin(0.22))


# Type Conversion
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
