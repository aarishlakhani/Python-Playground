# match statements
# gives a way to evaluate way and fires sections of code when the evaluate value matches
belt_colour = input("What is your ninja belt colour: ")
match belt_colour:
    case "white":
        print("Ninja Fledgeling")
    case "red":
        print("Intermediate Ninja")
    case "blue":
        print("Advanced Ninja")
    case "purple":
        print("Pro Ninja")
    case "black":
        print("Master Ninja")
    # use a default case incase the input doesnt match any of the above
    # use _: to show default case. No other syntax works
    case _:
        print("Belt Colour is Unknown")
