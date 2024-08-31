import random

option = ['rock', 'paper', 'scissor']
user_ip = input("Do you want to play?\n")
cscr = 0
uscr = 0

def logic(user):
    global cscr,uscr
    if user.lower() == "rock":
        if comp == "rock":
            print("computer:", comp)
            print("it's a tie")
        elif comp == "paper":
            print("computer:", comp)
            print("computer wins")
            cscr += 1
        else:
            print("computer:", comp)
            print("you win")
            uscr += 1

    elif user.lower() == "paper":
        if comp == "rock":
            print("computer:", comp)
            print("you win")
            uscr += 1
        elif comp == "paper":
            print("computer:", comp)
            print("it's a tie")
        elif comp == "scissor":
            print("computer:", comp)
            print("computer wins")
            cscr += 1

    elif user.lower() == "scissor":
        if comp == "paper":
            print("computer:", comp)
            print("you win")
            uscr += 1
        elif comp == "rock":
            print("computer:", comp)
            print("computer wins")
            cscr += 1
        elif comp == "scissor":
            print("computer:", comp)
            print("it's a tie")
    
    return cscr, uscr

while user_ip.lower() == "yes":
    print("ok, let's play")
    print("choose rock/paper/scissor")
    rand_int = random.randint(0, 2)
    comp = option[rand_int]
    userp = input("you: ")
    cscr,uscr=logic(userp)
    print("Do you want to play again?")
    user_ip = input("type here yes/no: ")
    if user_ip.lower() == "no":
        print("Your score:",uscr,"\n","Computer's score:",cscr)
        quit()
        
if user_ip.lower() == "no":
    quit()
else:
    print("Sorry, I can't understand.")