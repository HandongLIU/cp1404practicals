# Handong LIu
import random

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


import random


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = random.randrange(0, 100)
            print(score)
        elif choice == "P":
            score_status = determine_score(score)
            print(score_status)
        elif choice == "S":
            print(score * '*')
        else:
            print("farewell")
        print(MENU)
        choice = input(">>> ").upper()


def determine_score(score):
    if score < 0 or score > 100:
        score_status = "Invalid score"
    elif score >= 90:
        score_status = "Excellent"
    elif score >= 50:
        score_status = "Passable"
    else:
        score_status = "Bad"
    return score_status


main()
