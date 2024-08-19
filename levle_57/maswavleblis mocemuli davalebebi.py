print("Hello, World!")
name = input("Enter your name: ")
print("Hello, " + name + "!")
# This is a single-line comment

"""
This is a multi-line comment
You can write as many lines as you want
"""
print("Hello, World!")
if True:
    print("This is indented")
    print("This is also indented")
print("This is not indented")print("This is a very long line that needs to be broken \
into multiple lines for readability")
# This script prints "Hello, World!"
print("Hello, World!")  # This is the print statement

# This script takes user input and prints it
name = input("Enter your name: ")  # Get user input
print("Hello, " + name + "!")  # Print the greeting
def greet(name):
    """
    This function takes a name as input and returns a greeting
    """
    return "Hello, " + name + "!"

print(greet("John"))# print("This line is disabled")

# To re-enable it, simply remove the comment
print("This line is enabled")# This script has an intentional error: undefined variable
# print(x)  # This will raise a NameError because x is not defined
x = 5  # integer
y = 3.14  # float
name = "John"  # string
is_admin = True  # booleanx = 5  # integer
y = 3.14  # float
name = "John"  # string
is_admin = True  # boolean
x = 5
y = 10
x, y = y, x
print(x, y)  # Output: 10 5
x = 5
y = 10
x, y = y, x
print(x, y)  # Output: 10 5
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello, " + name + "! You are " + str(age) + " years old.")x = 5  # global variable

def foo():
    x = 10  # local variable
    print(x)  # Output: 10

foo()
print(x)  # Output: 5
# Valid variable names
x = 5
my_variable = 10
hello_world = "Hello, World!"

# Invalid variable names
# 2x = 5  # SyntaxError: invalid syntax
# my-variable = 10  # SyntaxError: invalid syntax
x = 5  # integer
y = 3.14  # float
name = "John"  # string
is_admin = True  # boolean
x = 5  # integer
y = float(x)  # convert to float
z = str(x)  # convert to string
print(y, z)  # Output: 5.0 5
x = 5
print(type(x))  # Output: <class 'int'>
x = 5  # integer
y = 3.14  # float
print(x + y)  # Output: 8.14
x = 5  # integer
y = 3.14  # float
print(x >