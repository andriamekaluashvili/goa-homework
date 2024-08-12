def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
    def division(a, b):
    result_addition = addition(5, 3)
print("Addition:", result_addition)

result_subtraction = subtraction(5, 3)
print("Subtraction:", result_subtraction)

result_multiplication = multiplication(5, 3)
print("Multiplication:", result_multiplication)

result_division = division(5, 3)
print("Division:", result_division)