def procedure_calculation(A:int,B:int,O:str):
    A=int(input("Please type a random number"))
    B=int(input ("Please type in another number"))
    O=input("Enter a to add, t to take-away, d to divide, m to multiply, p to power of or square the numbers you entered.")
    if O=='a':
        print(A + B)
    elif O=='t':
        print(A-B)
    elif O=='d':
        print(A/B)
    elif O=='m':
        print(A*B)
    elif O=='p':
        print(A**B)
    else:
        print("This function isn't possible")


procedure_calculation(1,2,'O')
procedure_calculation(3,4,'o')
procedure_calculation(5,6,'a')
procedure_calculation(7,8,'A')
