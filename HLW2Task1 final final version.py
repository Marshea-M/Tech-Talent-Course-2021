#Program to help a user decide what to wear, based on Data Flow Diagram

#ask the user if they are looking for daywear or evening wear
input_d_e=input("Are you looking for daywear or eveningwear? Please type day or evening ...")
#evening wear branch
if input_d_e=='evening':
    input_night_out=input("Night on the town? yes or no? ")
    if input_night_out=='yes':
        print("Wear the satin minidress! You'll look great!")
    elif input_night_out=='no':
        input_gala=input("Fancy gala, black-tie or ball? yes or no? ")
        if input_gala=='yes':
            input_weather=input("Do you think it will be cold? yes or no? ")
            if input_weather=='yes':
                print("Okay then wear the jacquard blazer. ")
            elif input_weather=='no':
                print("Then you should wear the open back gown! ")
        elif input_gala=='no':
            input_restaurant=input("Dinner at a restaurant? yes or no? ")
            if input_restaurant=='yes':
                print("Wear the light blue-fitted knit top you bought three months ago. Yes that one. ")
            elif input_restaurant=='no':
                print("Pyjamas might be your best option.")
#daywear clothes branch
elif input_d_e=='day':
    input_casual=input("Is this for a casual occasion? yes or no? ")
if input_casual=='yes':
    input_weather=input("Do you think it will be cold? yes or no? ")
    if input_weather=='yes':
        print("Then wear your hoodie, flare trousers and lots of jewellry.")
    elif input_weather=='no':
        print("Blue jeans and a crinkle crop top.")
elif input_casual=='no':
    input_work=input("Is this for work?")
    if input_work=='yes':
        print("Wear a cosy turtleneck with straightleg trousers.")
    elif input_work=='no':
        input_party=input("Are you dressing for a wedding or a pary?")
        if input_party=='yes':
            print("You can maybe get away with that Puffy Sleeve Square neck top.")
        elif input_party=='no':
            input_exercise=input("Do you need an outfit for exercise,outdoor sports or hiking? Please type yes or no")
            if input_exercise=='no':
                print("Yeah I didn't think so we don't exercise haha.")
            while input_exercise=='yes':
                input_exercise=input("Are you sure because we don't really exercise haha. Do you need an outfit for exercise,outdoor sports or hiking? Please type yes or no")
else:
    print("I hope this helped!")
