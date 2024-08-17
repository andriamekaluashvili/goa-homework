1.def substract(x, y):
    return x - y

# მაგალითის გამოყენება
result = substract(10, 5)
print(result)  # ეს გამოიტანს: 5
2.
def combine_words(word1, word2):
    return word1 + " " + word2

# მაგალითის გამოყენება
result = combine_words("გამარჯობა", "მეგობარო")
print(result)  # ეს გამოიტანს: "გამარჯობა მეგობარო"
3.
def calculate_area(length, width):
    return length * width

# მაგალითის გამოყენება
result = calculate_area(4, 6)
print(result)  # ეს გამოიტანს: 24
4.
def greet(name):
    return f"გამარჯობა, {name}"

# მაგალითის გამოყენება
result = greet("ანა")
print(result)  # ეს გამოიტანს: "გამარჯობა, ანა"
5.
def check_number_size(number):
    if number > 10:
        return "დიდია"
    else:
        return "პატარა"

# მაგალითის გამოყენება
result = check_number_size(9)
print(result)  # ეს გამოიტანს: "პატარა"
6.
def good_day():
    return "კარგი დღე გქონდეს!"
7.
def sum_numbers(a, b):
    return a + b

# ფუნქციის გამოძახება არგუმენტ
def cube_number(number):
    return number ** 3
8.
# ფუნქციის გამოძახება არგუმენტით 3
print(cube_number(3))  # გამოიტანს: 27
9.
def best_message():
    return "საუკეთესო ხარ!"

# ფუნქციის გამოძახება
print(best_message())  # გამოიტანს: საუკეთესო ხარ!
10.
def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

# ფუნქციის გამოძახება არგუმენტით 8
print(even_or_odd(8))  # გამოიტანს: ლუწი