# handong LIu

import random

line = 6
MIN = 1
MAX = 45

def main():
    number_of_quick_picks = int(input("How many Quick Picks: ?"))
    while number_of_quick_picks < 0:
        print("error")
        number_of_quick_picks = int(input("How many Quick Picks: ?"))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(line):
            number = random.randint(MIN,MAX)
            while number in quick_pick:
                number = random.randint(MIN,MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))
main()