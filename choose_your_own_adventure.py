name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer1 = input("You're on a dirt road, it has come to an end, and you can go left or right. Which way? ").lower()

if answer1 == "left":
    answer2 = input("You come to a river.")
elif answer1 == "right":
    print()
else:
    print("Not a valid answer; you lose!")