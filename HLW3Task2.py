def mark_grade():
    output=int(input("Please type in your percentage mark for this semester."))
    if output>70:
        print("Your grade is an A")
    elif output>60:
        print("Your grade is an B")
    elif output>50:
        print("Your grade is a C")
    elif output>40:
        print("Your grade is a D")
    elif output>30:
        print("Your grade is an E")
    else:
        print("Your grade is a U")

    return output

message=mark_grade()
print("If you need anymore feedback on the work you handed in, please do not hesitate to send an email, to arrange a 1:1 session.") 
