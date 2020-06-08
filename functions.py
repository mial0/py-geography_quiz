import random
def play_game():
    countries_cities = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome", "Austria": "Vienna",
                        "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana"}
    country_list = list(countries_cities.keys())
    country = random.choice(country_list)
    capital_city = countries_cities[country]

    while True:
        guess = input("What is the capital city of %s ?" %country)
        if guess.lower() == capital_city.lower():
            print("Correct answer!")
            break
        elif guess.lower() == "exit":
            print("Game over! Correct answer is %s " %capital_city)
            break
        else:
            print("Wrong answer. Try again!")