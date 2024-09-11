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
import random
mychoice=input("choose 0 for rock, 1 for paper or 2 for scissors\n")
mychoice=int(mychoice)
signs=[rock,paper,scissors]
print(signs[mychoice])
computer=random.randint(0,2)
print(f'"i will go for..." \n{signs[computer]}')
if mychoice==0 and computer==2:
    print(f'you win T-T')
elif computer>mychoice:
    print("you lost human•ᴗ• ")
elif computer==mychoice:
    print("good game ¬_¬ ")
else:
    print("you win")
print( )
print("thanks for playing with me human")