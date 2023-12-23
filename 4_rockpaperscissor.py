import random
rock = '''
    ________
---'    ____)
       (_____)
       (____)
       (___)
---'__(__)
'''
paper = '''
    ________
---'    ____)____
           ______)
           _______)
           ______)
           _____)
---'__________)
'''

scissors = '''
    _______
---'   ____)_____
          _______)
      ____________)
      (____)
---'__(___)
'''
images = [rock, paper, scissors]
input_user = int(input("what do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS.\n  "))
if input_user >= 3 or input_comp <0:
    print("You typed wrong")
else:
    print(images[input_user])
    input_comp = random.randint(0, 2)
    print("computer choose: ")
    print(images[input_comp])

    if input_user == 0 and input_comp == 2:
        print("You win")
    elif input_comp == 0 and input_user ==2:
        print("you lose")
    elif input_comp > input_user:
        print("you lose.")
    elif input_comp < input_user:
        print("you won")
    elif input_comp==input_user:
        print("Draw.")



