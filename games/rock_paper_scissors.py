import random

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


options = ["rock", "paper", "scissors"]

print("Your options are: ")
for option in options:
    print(option)
user_choice = input("What do you choose? \n")
print("You chose: ", user_choice)
computer_choice = random.choice(options)
print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
    exit()

if user_choice == "rock":
    if computer_choice == "paper":
        print("You lose!")
        exit()
    elif computer_choice == "scissors":
        print("You win!")
        exit()

if user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
        exit()
    if computer_choice == "scissors":
        print("You lose!")
        exit()

if user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
        exit()
    if computer_choice == "rock":
        print("You lose!")
        exit()
