# This program prompts the user to enter a day of the week and uses a match-case statement to print a message based on the input.
day = str(input("Enter a day of the week: ")).lower()

match day:
    case "monday":
       print("Damn, it's Monaday!")
    case "tuesday":
        print("It's Tuesday, let's keep grinding.")
    case "wedsday":
        print("It's wednesday, well begun is half done.")
    case "thursday":
        print("It's Thursday, let's wrap up the week.")
    case "friday":
        print("It's friday, let's finish strong.")
    case "saturday" | "sunday":
        print("Ladies and gentlemen, it's a weekend!")
    case _:
        print("You didn't enter a valid day of the week.")# End of program)
        
    


