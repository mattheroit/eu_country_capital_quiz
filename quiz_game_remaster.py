import random, os, time

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


# Vyprázdnit konzoli
def cls():
    os.system("cls" if os.name == "nt" else "clear")


# Gameplay
def game_main(endlessMode: bool):
    cls()
    print(f"{brgt_magenta}Let's start!")
    remainingCapitals = countryCapital.copy()
    score = 0

    gameLenght = range(len(countryCapital))
    if endlessMode:
        gameLenght = range(1000000000)

    for _ in gameLenght:
        countryCapitalPair = random.choice(list(remainingCapitals.items()))
        country = countryCapitalPair[0]
        capital = countryCapitalPair[-1]
        if not endlessMode:
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

    if score == len(countryCapital) and not endlessMode:
        print(f"{brgt_yellow}You won!")

    # Konec hry
    print(f"{white}Your score is {brgt_magenta}{score}")
    playTheGame()


def pickGameMode():
    print(f"{white}Before we start, please pick a game mode ")
    print(f"{white}Classic mode (C)")
    print(f"{white}Endless mode (E)")
    while True:
        endless = input(f"{white}Mode (C/E): ")
        if endless.lower() == "e":
            game_main(True)
            break
        elif endless.lower() == "c":
            game_main(False)
            break


# Hrát?
def playTheGame():
    play = input(f"{white}{name}, do you want to play? {yesOrNoStr}: ")
    if play.lower() == "n":
        print(goodbyeStr)
        time.sleep(3)
        quit()
    pickGameMode()


# Začátek hry
print(f"{brgt_magenta}Welcome to the EU country capital quiz game!")
name = input(f"{white}Enter your name: ")
playTheGame()
