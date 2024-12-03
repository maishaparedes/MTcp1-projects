import random 
score = 0

com1 = ["rock", "paper" , "scissors"]
inside = random.choice(com1)
user = input("Choose rock paper or scissors!")

while user not in ["rock, paper, scissors"]:
    print("Try again")
    user = input("Rock paper scissors")
    if user in ["rock, paper, scissors"]: 
        break
    
ask = input("Would you like to play?:\n ")
if ask == "no":
    print("Okay, you don't gotta play, bye!")
while ask == "yes":
    if user == "scissors" and inside == "rock":
        print("You lost this part")
        score -= 1
        print(score)
    elif user == "rock" and com1 == "scissors":
        print("You won this part")
        score += 1
        print(score)
    elif user == "paper" and inside == "scissors":
        print("You lost this part")
        score -= 1
        print(score)
    elif user == "scissors" and inside == "paper":
        print("You won this part")
        score += 1
        print(score)
    elif user == "paper" and inside == "scissors":
        print("You lost this part")
        score -= 1
        print(score)
    elif user == "rock" and inside == "paper":
        print("You lost this part")
        score -= 1
        print(score)
    elif user == "paper" and inside == "rock":
        print("You lost this part")
        score += 1
        print(score)
    else:
        print("it is a tie. No points")







