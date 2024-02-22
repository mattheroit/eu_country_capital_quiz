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

# Texty
yesOrNoStr = f"{white}({brgt_green}y{white}/{red}n{white})"
goodbyeStr = f"{white}Goodbye!"


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
            print(f"{white}Correct!")
        else:
            print(f"{white}Wrong!")
            print(
                f"{white}The capital of {brgt_yellow}{item[0]} {white}is {brgt_cyan}{item[-1]}"
            )
            break

    # Konec hry
    print(f"{white}Your score is {brgt_magenta}{score}")
    play_again = input(f"{white}{name}, do you want to play again? {yesOrNoStr}: ")
    if play_again.lower() == "y":
        game_main()
    else:
        print(goodbyeStr)
        quit()


# Začátek hry
print(f"{brgt_magenta}Welcome to the quiz game!")
name = input(f"{white}Enter your name: ").capitalize()
game = input(f"{white}{name}, do you want to play? {yesOrNoStr}: ")
if game.lower() == "n":
    print(goodbyeStr)
    quit()
else:
    game_main()
