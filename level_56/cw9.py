def print_min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    print("Minimum number:", minimum)
    print("Maximum number:", maximum)
    numbers = [2, 5, 1, 8, 4]
print_min_max(numbers)