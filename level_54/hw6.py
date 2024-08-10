def check_number():
    number = float(input("Enter a number: "))
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"

result = check_number()
print(result)