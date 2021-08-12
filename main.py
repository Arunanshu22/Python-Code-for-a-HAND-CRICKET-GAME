import time
class bcolors:
    HEADER = '\033[95m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DARKGREY='\033[90m'
    LIGHTRED='\033[91m'
    LIGHTGREEN='\033[92m'
    LIGHTGREY='\033[37m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # Background colors:
    LIGHTGREYBG='\033[47m'
    PURPLEBG='\033[45m'
    ORANGEBG='\033[43m'
    GREYBG = '\033[100m'
    REDBG = '\033[101m'
    GREENBG = '\033[102m'
    YELLOWBG = '\033[103m'
    BLUEBG = '\033[104m'
    PINKBG = '\033[105m'
    CYANBG = '\033[106m'
print ("Time to start HAND CRICKET\n")
time.sleep(1)
print ("Rules are simple! If you are batting make sure you dont end up typing same number as of computer! If you are bowling try guessing number chosen by computer\n")
time.sleep(3)
print ("The Number must be within 0 to 10"'\n')
time.sleep(1)
print ("Score keeps adding up till you are out!!\n")
time.sleep(1)
print ("All the best now !!")
import random
choice_man =""
i = 1
print ("Toss time\n")
man_choice = input ("Heads or Tails\n")
coin = ["heads" , "tails"]
toss = random.choice (coin)
if (man_choice == toss):
    print (bcolors.GREEN+"You won the toss"+bcolors.END)
    choice_man = input("Wanna be Dhoni or Bumrah..... I mean wanna bat or bowl.....\n")
    choice_man = choice_man.lower()
else:
    print (bcolors.RED+"Computer won the toss!!"+bcolors.END)
    bat_bowl = ["bat" , "bowl"]
    choice_comp = random.choice(bat_bowl)
    print ("And choose to ", bcolors.BLUE+choice_comp+bcolors.END)
    if(choice_comp == "bat"):
        choice_man = "bowl"
if (choice_man == "bowl"):
    while True:
        if (i == 1):
            comp_score = 0
            man_score = 0
            print("Now",bcolors.YELLOW+"Computer"+bcolors.END, "will Bat first")
            while True:
                comp = random.randint(0,10)
                man = int(input ("Enter your number \n"))
                if man not in (0,1,2,3,4,5,6,7,8,9,10):
                    print("Invalid input")
                    continue
                else:
                    pass
                if  (comp != man):
                    print(bcolors.RED+"Nope"+bcolors.END, "the number was",comp)
                    comp_score += comp
                else:
                    print(bcolors.GREENBG+"HOWZATT!!! You got computers wicket!!!"+bcolors.END)
                    break
            print(bcolors.YELLOW+"Computer net score was"+bcolors.END,comp_score,bcolors.YELLOW+"points"+bcolors.END)
            print (" Get ready now..... Gotta rock batting too.....")
            while (comp_score >= man_score):
                comp = random.randint(0,10)
                man = int (input ("Enter a number"))
                if (man not in (0,1,2,3,4,5,6,7,8,9,10)):
                    print("Invalid input")
                    continue
                else:
                    pass
                if (comp == man):
                    print (bcolors.REDBG+"NOOOOOOO!!!!! Computer got your wicket!!!!"+bcolors.END)
                    difference = comp_score - man_score
                    if (difference == 0):
                        difference == 1
                    print (bcolors.REDBG+"Computer won by a score of "+bcolors.END,difference,bcolors.REDBG+"points"+bcolors.END)
                    i = int (input ("Press 1 to play again and press 2 quit......\n"))
                    if (i == 1):
                        continue
                    else:
                        print("Bye Bye!!")
                        break
                else:
                    man_score += man
                    difference = comp_score - man_score
                    if (difference<0):
                        difference = "no more"
                    if (difference == 0):
                        difference == 1
                    print (bcolors.YELLOW+"Nice shot.... You need "+bcolors.END, man_score,bcolors.YELLOW+"and you need"+bcolors.END,difference,bcolors.GREEN+" more points to win"+bcolors.END)
            else:
                print(bcolors.LIGHTGREEN+"Lessssgooooo!!! You WON!!!"+bcolors.END)
                i = int (input("Press 1 to play again and press 2 quit......\n"))
        else:
            break
else:
    while True:
        if (i == 1):
            comp_score = 0
            man_score = 0
            print("Now",bcolors.GREEN+"You"+bcolors.END,"are gonna bat")
            while True:
                comp = random.randint(0,10)
                man = int(input ("Enter a number \n"))
                if man not in (0,1,2,3,4,5,6,7,8,9,10):
                    print("Invalid input")
                    break
                else:
                    pass
                if  (comp != man):
                    print(" Nice Shot....")
                    man_score += man
                    print ("Your current score is ",man_score,"points")
                else:
                    print(bcolors.RED+"NOOOOOOO!!!!! Computer got your wicket!!!"+bcolors.END)
                    break
            print("You had scored",man_score)
            print (" Now Computer\'s turn to bat")
            while (comp_score <= man_score):
                comp = random.randint(0,10)
                man = int (input ("Enter your guess"))
                while (man not in (0,1,2,3,4,5,6,7,8,9,10)):
                    print("Invalid input")
                else:
                    pass
                if (comp == man):
                    print (bcolors.GREENBG+"HOWZATT!!! You got computers wicket!!!"+bcolors.END)
                    difference = man_score - comp_score
                    if (difference == 0):
                        difference == 1
                    print (bcolors.LIGHTGREYBG+"You won by a difference of"+bcolors.END,difference,bcolors.LIGHTGREYBG+"points"+bcolors.END)
                    i = int (input ("Press 1 to play again and press 2 quit......\n"))
                    if (i == 1):
                        continue
                    else:
                        break
                else:
                    comp_score += comp
                    difference = man_score - comp_score
                    if (difference == 0):
                        difference == 1
                    print ("Nope the number was ",comp)
                    print (" Computers score is ", comp_score,"and it needs",difference,"points to win..... Watchout dont let computer win.......")
            else:
                print(bcolors.REDBG+"Good try!! Computer won the match...... Play again and make computer feel the wrath!!!!"+bcolors.END)
                print(bcolors.LIGHTRED+"Computer had won by a difference of"+bcolors.END,difference,bcolors.LIGHTRED+"points"+bcolors.END)
                i = int (input("Press 1 to play again and press 2 quit......\n"))
        else:
            break