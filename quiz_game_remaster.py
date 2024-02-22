import random

# Slovník země/město
countryCapital = {
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Latvia": "Riga",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Malta": "Valletta",
    "Netherlands": "Amsterdam",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
}

# Barvy
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
brgt_red = "\033[0;91m"
brgt_green = "\033[0;92m"
brgt_yellow = "\033[0;93m"
brgt_magenta = "\033[0;95m"
brgt_cyan = "\033[0;96m"
white = "\u001b[0m"


# Hlavní část
def game_main():
    print(f"{brgt_magenta}Let's start!")
    score = 0
    drawn = set()
    while True:
        item = random.choice(list(countryCapital.items()))
        if score == len(countryCapital):
            print(f"{brgt_yellow}You won!")
            break
        elif item in drawn:
            continue
        else:
            drawn.add(item)
            capital = input(
                f"{white}What is the capital of {brgt_cyan}{item[0]}{white}? "
            ).capitalize()

        if capital == item[-1]:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
            print(f"The capital of {item[0]} is {item[-1]}")
            break

    # Konec hry
    print(f"{white}Your score is {brgt_magenta}{score}")
    play_again = input(
        f"{white}{name}, do you want to play again? ({brgt_green}y{white}/{red}n{white}): "
    )
    if play_again.lower() == "y":
        game_main()
    else:
        print(f"{white}Goodbye!")
        quit()


# Začátek hry
print(f"{brgt_magenta}Welcome to the quiz game!")
name = input(f"{white}Enter your name: ").capitalize()
game = input(f"{name}, do you want to play? ({brgt_green}y{white}/{red}n{white}): ")
if game.lower() == "n":
    print("Goodbye!")
    quit()
else:
    game_main()
