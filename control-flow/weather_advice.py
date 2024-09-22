# weather_advice.py

def get_weather_advice(weather):
    if weather == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

def main():
    # Prompting the user for weather input
    user_weather = input("What's the weather like today? (sunny/rainy/cold): ")
    # Getting clothing recommendation based on the weather
    advice = get_weather_advice(user_weather)
    # Outputting the clothing recommendation
    print(advice)

if __name__ == "__main__":
    main()
