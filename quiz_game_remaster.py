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
white = "\u001b[0m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
brgt_red = "\033[0;91m"
brgt_green = "\033[0;92m"
brgt_yellow = "\033[0;93m"
brgt_magenta = "\033[0;95m"
brgt_cyan = "\033[0;96m"

# Texty
yesOrNoStr = f"{white}({brgt_green}y{white}/{red}n{white})"
goodbyeStr = f"{white}Goodbye!"


# Hrát/Hrát znovu?
def playTheGame():
    play = input(f"{white}{name}, do you want to play? {yesOrNoStr}: ")
    if play.lower() == "n":
        print(goodbyeStr)
        quit()
    else:
        game_main()


# Hlavní část
def game_main():
    print(f"{brgt_magenta}Let's start!")
    remainingCapitals = countryCapital.copy()
    score = 0
    for _ in range(len(countryCapital)):
        countryCapitalPair = random.choice(list(remainingCapitals.items()))
        country = countryCapitalPair[0]
        capital = countryCapitalPair[-1]
        del remainingCapitals[country]

        answer = input(
            f"{white}What is the capital of {brgt_cyan}{country}{white}? "
        ).capitalize()

        if answer != capital:
            print(f"{white}Wrong!")
            print(
                f"{white}The capital of {brgt_yellow}{country} {white}is {brgt_cyan}{capital}"
            )
            break

        score += 1
        print(f"{white}Correct!")

    if score == len(countryCapital):
        print(f"{brgt_yellow}You won!")

    # Konec hry
    print(f"{white}Your score is {brgt_magenta}{score}")
    playTheGame()


# Začátek hry
print(f"{brgt_magenta}Welcome to the quiz game!")
name = input(f"{white}Enter your name: ")
playTheGame()
