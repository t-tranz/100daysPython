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

# Write your code below this line 👇
picture = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

print(f"Computer chose: \n {picture[computer]}\n You chose \n {picture[user]}")
if user == computer:
    print("Game draw")
elif user == 0 and computer == 1:
    print("You lose!")
elif user == 0 and computer == 2:
    print("You win!")
elif user == 1 and computer == 0:
    print("You win!")
elif user == 1 and computer == 2:
    print("You win!")
elif user == 2 and computer == 0:
    print("You lose!")
elif user == 2 and computer == 1:
    print("You win!")

