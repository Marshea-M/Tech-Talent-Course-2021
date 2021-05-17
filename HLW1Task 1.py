import random as random
random_number=random.randint(1,10)
print("Hi, here is a random number:", random_number)

user_name_input=input("What is your name?")
user_number_input=input("Please guess a number between 1 and 10.")
if user_number_input ==random_number: 
    print("You have guessed correctly!")
else:
    print("Sadly, you have not guessed correclty.")