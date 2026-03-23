import json
import re

def display_title():
    print('Hello! Welcome to "Text Based Adventure" by Maxwell Monk.')
    print('This is a small text based adventure set in a world where only the mathematically\nproficient can survive, you, the adventurer, will follow along a path to a faraway kingdom.\nAlong the way you will face many mathematical challenges, but be careful! A bad choice could cost you your life.')
    print('Good luck adventurer!')
    print()

def get_user_name():
    global user_name, player_score
    while True:
        user_name = input('Please enter your name brave adventurer: ')
        if not re.match("^[A-Za-z]*$", user_name):
            print('Error! Make sure to use only letters in your name')
        else:
            print('Hello ' + user_name + ' lesser students will tell tales of your mathematical prowess. Let us begin. ')
            print()
            break

def storeplayerscores():
    global user_name, player_score
    try:
       with open("player_data.json", "r")as f:
        data = json.load(f)
        if not isinstance(data, dict):
            data = {}
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data.setdefault(user_name, []).append(player_score)
    with open("player_data.json", "w") as f:
        json.dump(data, f, indent=2)



def readplayerscores():
    try:
        with open("player_data.json", "r") as f:
            player_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No saved scores found.")
        return

    for names, scores in player_data.items():
            if isinstance(scores, int):
                scores = [scores]
            print(f"{names}: {', '.join(map(str, scores))}")


def main():
    global player_score, user_name
    player_score = 0
    decisions = []
    display_title()
    get_user_name()
    answer1 = int(input('Soon after your departure, along a trail in an empty forest, you come to an intersection with four labeled paths, one, two, three, and four\nYou also see a sign planted in the ground, it reads "Only those worthy may follow the path to math kingdom." \n16 x 2 / 8 will reveal the truth to you.\nWhich path do you choose? '))
    decisions.append("Chose path " + str(answer1))
    print()
    if answer1 != 4:
        print('You go down the path of your choosing, but it simply leads to a dead end. Better luck next time!')
        print()
        storeplayerscores()
    else:
        player_score += 1
        print('The math lords are pleased with your decision. Onward!')
        print('Your score has increased by 1')
        print()
        answer2 = input('Along your travels, you come accross a dark cavern with the phrase "MATH KINGDOM --->"\nengraved in a nearby rock. Inside you find it leads to a dead end with three ancient levers on the wall.\nAbove each one you see "e" "pi" and "rad." More engravings read "3.14159 = ?"\nWhich lever do you choose to flip?')
        decisions.append("Chose path " + str(answer2))
        if answer2 != "pi":
            print('A hatch on the ceiling behind you suddenly opens and drops boulders, blocking your exit. This marks the end of your journey\nBetter luck next time!')
            storeplayerscores()
        else:
            player_score += 1
            print('A hidden wall opens within the cavern, allowing you to reach the other side and get back to the surface.')
            print('The math lords are pleased with your decision. Onward!')
            print('Your score has increased by 1')
            print()
            answer3 = input('Finally, after exiting the cavern and following the route which it led to, you come across a large gate with a guard outside.\nAs you approach him he says "Only those educated in the history of our craft may enter!"\n"Who is the most known inventor of calculus?"')
            decisions.append("Chose " + str(answer3))
            if answer3.lower() != "isaac newton":
                print('The guard says firmly "You are not worthy! Now begone!" Better luck next time!')
                storeplayerscores()
            else:
                player_score += 1
                print('The guard says with glee "You are truly worthy, welcome to Math Kingdom!" \nHe opens the gates and you enter with ease.')
                print('Congratulations you win!')


    print()
    print('Your final score was ' + str(player_score))
    print('Paths chosen: ' + str(decisions))
    storeplayerscores()

    print()
    print('--- ALL PLAYER SCORES ---')
    readplayerscores()


while True:
    main()
    replay = input("Play again? (y/n): ")
    if replay.lower() != 'y':
        print('Thanks for playing my game ' + user_name + '!')
        break

