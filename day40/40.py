# Take input from the user
numbers = []
for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

# Filter the list into even and odd numbers
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Print the even and odd numbers
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)