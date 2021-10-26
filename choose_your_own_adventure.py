name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You're on a dirt road, it has come to an end, and you can go left or right. Which way? ").lower()

if answer == "left":
    answer = input("You come to a river; you walk around it or swim across it. Type 'walk' or 'swim': ").lower()

    if answer == 'swim':
        print("You swam across and were abducted by aliens.")

    elif answer == 'walk':
        print("You walked across for miles and ran out of supplies, so you lost the game.")

    else:
        print("Not a valid answer; you lose!")

elif answer == "right":
    answer = input("You've come to a wobbly bridge; do you want to cross it or go back? Type 'cross' or 'go back': ").lower()
    
    if answer == 'cross':
            answer = input("You swam across and met a stranger. Will you talk to them? Answer 'yes' or 'no.'").lower()
            
            if answer == "yes":
                print("You talked to the stranger and they gave you the map. You win!!")
            elif answer == "no":
                print("You ignored the stranger, offending them, so you lose.")
            else:
                print("Not a valid answer; you lose!")

    elif answer == 'go back':
        print("You walked back for miles and ran out of supplies, so you lost the game.")

    else:
        print("Not a valid answer; you lose!")

else:
    print("Not a valid answer; you lose!")

print("Thank you for playing the game, ", name)