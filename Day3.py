print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#write your code below
print(".........................")
print("You are going along a narrow path in the mist of a dark forrest, you end up in a dead end")
first = input("Do you want to go Left? or Right? ")
if first.lower() == "left":
    print("It seems like you choose a safe path. You stay on that path for some time until you stumble a lake")
    second = input("Do you want to Swim? or Wait? ")
    if second.lower() == "swim":
        print("You swimmed to a small island and come across a house with three doors of entry")
        third = input("Which door do you want to enter? Red, Yellow, or Blue? ")
        if third.lower() == "red":
            print("Burned by fire. Game Over.")
        elif third.lower() == "yellow":
            print("You Win!")
        elif third.lower() == "blue":
            print("Eaten by beasts. Game Over.")

    else:
        print("You were attacked by a trout. Game over.")

else:
    print("You fell into a hole. Game Over.")
    