import random

choices = ['ქვა' , 'ქაღალდი' , 'მაკრატელი']
(variable) computer_choice: str
computer_choice = random.choice(choices)



user_choice = input("შეიყვნეთ თქვენი არჩევანი (ქვა, ქაღალდი, მაკრატელი): ")

while user_choice not in choices:
    print("არასწორი არჩევანი. სცადეთ თავიდან.")
    user_choice = input("შეიყვანეთ თქვენი არჩევანი (ქვა, ქაღალდი, მაკრატელი): ")


print("თქვენ აირჩიეთ:",user_choice)  
print("კომპიუტერმა აირჩია: ", computer_choice)

if user_choice == computer_choice:
    print("ფრეა!")
elif (user_choice == 'ქვა' and computer_choice == 'მაკრატელი')
     (user_choice == 'ქაღალდი' and computer_choice == 'ქვა')
     (user_choice == 'მაკრატელი' and computer_choice == 'ქაღალდი')
     print("თქვენ მოიგეთ!")


else:
    print("კომპიუტერმა მოიგო!")
     