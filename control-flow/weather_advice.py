# Prompt the user to input today's weather condition
weather_today = str(input("What's the weather like today? sunny/rainy/cold: ")).lower()
# Provide advice based on the weather condition
if weather_today == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_today == "rainy":
    print("Don't forget the umbrella and a raincoat.")
elif weather_today == "cold":
    print(" Make sure to wear a warm jacket and a scarf.")
else:
    print("sorry, I don't have advice for that weather condition.")
