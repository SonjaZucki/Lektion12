import random
import json
import datetime

name: str = input("Hi, what is your name? ")


def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    wrong_guesses = []

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"name": name, "secret": secret, "attempts": attempts, "guesses": wrong_guesses,
                               "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

        wrong_guesses.append(guess)


def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list


while True:
    selection = input("Hi " + name + ", do you want to A) play a new game, B) see the best scores or C) quit playing? ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            score_text = "{0} had {1} attempts on the secret number {2}, with the wrong guesses {3} on {4}".format(
                score_dict.get("name"),
                str(score_dict.get("attempts")),
                score_dict.get("secret"),
                score_dict.get("guesses"),
                score_dict.get("date"))
            print(score_text)
    else:
        break

print("Okay, bye!")