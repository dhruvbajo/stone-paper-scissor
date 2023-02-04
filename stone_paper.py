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
user=int(input("what do you choose?\n Type 0 for ROCK\n Type 1 for PAPER\n Type 2 for SCISSORS: "))
if user==0:
   print(rock)
elif user==1:
   print(paper)
else:
   print(scissors)
print("COMPUTER CHOSE:\n")
rc=random.randint(0,2)
if rc==0:
  print(rock)
elif rc==1:
  print(paper)
else:
  print(scissors)

if rc==user:
  print("TIED")
elif user==0 and rc==2:
  print("YOU WIN!")
elif user==1 and rc==0:
  print("YOU WIN!")
elif user==2 and rc==1:
  print("YOU WIN!")
else:
  print("YOU LOSE")