# Prompt the user to input today's weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide advice based on the weather condition
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget the umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm jacket and a scarf.")
else:
    print("Sorry, I don't have advice for that weather condition.")
