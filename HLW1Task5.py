user_input_number_a=int(input("Please type a random number"))
user_input_number_b=int(input ("Please type in another number"))

input_a=int(user_input_number_a)
input_b=int(user_input_number_b)

user_input_operator=input("Enter a to add, t to take-away, d to divide, m to multiply, p to power of or square the numbers you entered.")


if user_input_operator=='a':
    print(user_input_number_a + user_input_number_b)
elif user_input_operator=='t':
    print(user_input_number_a-user_input_number_b)
elif user_input_operator=='d':
    print(user_input_number_a/user_input_number_b)
elif user_input_operator=='m':
    print(user_input_number_a*user_input_number_b)
elif user_input_operator=='p':
    print(user_input_number_a**user_input_number_b)
else:
    print("This function isn't possible")
