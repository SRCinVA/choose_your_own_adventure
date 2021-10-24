name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer1 = input("You're on a dirt road, it has come to an end, and you can go left or right. Which way? ").lower()

if answer1 == "left":
    answer2 = input("You come to a river; you walk around it or swim across it. Tyoe 'walk' or 'swim': ")

    if answer2 == 'swim':
        print("You swam across and were abducted by aliens.")

    elif answer2 == 'walk':
        print("You walked across for miles and ran out of supplies, so you lost the game.")

    else:
        print("Not a valid answer; you lose!")

elif answer1 == "right":
    print("You've come to a wobbly bridge; do you want to cross it or go back? Type 'cross' or 'go back': ")
    if answer2 == 'cross':
            print("You swam across and were abducted by pirates.")

    elif answer2 == 'go back':
        print("You walked back for miles and ran out of supplies, so you lost the game.")

    else:
        print("Not a valid answer; you lose!")


else:
    print("Not a valid answer; you lose!")