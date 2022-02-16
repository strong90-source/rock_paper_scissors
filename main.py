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

#Write your code below this line 👇

#Create a list of the images above and store it in a variable
game_list = [rock, paper, scissors]

#Ask for the user's input and print the image
user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choise >= 3 or user_choise < 0:
  print("You typed an invalid number, you lose!!!")
else:
  print(game_list[user_choise])

#Use random to generate a random int number and print the image 
  computer_choice = random.randint(0, 2)
  print(f"computer choose:")
  print(game_list[computer_choice])

#If statments for the logic of who wins the game

  if user_choise == 0 and computer_choice == 2:
    print("You Win! 😁")
  elif computer_choice ==0 and user_choise == 2:
    print("You lose!😒")
  elif computer_choice > user_choise:
    print("You lose!😒")
  elif computer_choice < user_choise:
    print("You Win! 😁")
  elif computer_choice == user_choise:
    print("You draw the game!😁😒")
  