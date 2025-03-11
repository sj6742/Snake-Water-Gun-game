import random

'''
1 = snake
-1 = water
0 = gun
'''

computer = random.choice([-1, 0, 1])
youDict = {"s": 1, "w": -1, "g": 0}
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"}

youstr = input("Enter Your Choice (s for Snake🐍, w for Water💧, g for Gun🔫): ").lower()


if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    print(f"You Chose {reversedDict[you]}\nComputer chose {reversedDict[computer]}")

    if computer == you:
        print("It's a Draw!!")
    else:
        if  (computer == -1 and you == 1) or \
            (computer == 1 and you == 0) or \
            (computer == 0 and you == -1):
            print("You Win!!")
        else:
            print("You Lose!!")
