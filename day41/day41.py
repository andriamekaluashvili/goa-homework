# Function to calculate the sum of multiples of five
def sum_of_multiples_of_five(numbers):
    # Initialize sum variable
    sum_multiples_of_five = 0
    
    # Iterate over each number in the list
    for number in numbers:
        # Check if the number is a multiple of five
        if number % 5 == 0:
            # Add the number to the sum
            sum_multiples_of_five += number
    
    # Return the sum of multiples of five
    return sum_multiples_of_five

# Test the function
numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
result = sum_of_multiples_of_five(numbers)
print("Sum of multiples of five:", result)