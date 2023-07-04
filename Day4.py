# This code is a simple rock, paper and scissors game. This is an interactive game where a user is up against the code, which randomly selects an output

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
random_num = random.randint(0, 2)

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

together = [rock, paper, scissors]

if player == 0:
    print(rock)
    print("Computer chose: ")
    print(together[random_num])
    if random_num == 1:
        print("You lose")
    elif random_num == 0:
        print("Draw")
    elif random_num == 2:
        print("You win")

elif player == 1:
    print(paper)
    print("Computer choose: ")
    print(together[random_num])
    if random_num == 2:
        print("You lose")
    elif random_num == 1:
        print("Draw")

    else:
        print("You win")
elif player == 2:
    print(scissors)
    print("Computer choose: ")
    print(together[random_num])
    if random_num == 0:
        print("You lose")
    elif random_num == 2:
        print("draw")

    else:
        print("You win")
