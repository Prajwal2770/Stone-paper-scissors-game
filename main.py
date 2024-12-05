'''
1=stone
-1=paper
0=scissors
'''

import random
while True: 
    a=input("Want to start or continue the came(y for start or continue and q for end): ")
    if a=="q".lower():
        break
    elif a=="y".lower():
        computer=random.choice([1,-1,0])
        youstr=input("Enter your choice (stone, paper, scissors): ")
        youdict = {"stone":1,"paper":-1,"scissors":0}
        reversedict = {1:"stone",-1:"paper",0:"scissors"}
        you = youdict[youstr]

        print(f"You chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

        if(computer==you):
            print("Draw")

        else:

            if(computer == 1 and you == -1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
                print("You Lose")


            elif(computer == -1 and you == 0) or (computer == -1 and you == 1) or (computer == 0 and you == 1):
                print("You Win")


            else:
                print("Something went wrong")