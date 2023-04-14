import random #Random selection for AI
import time #Time delay
import colorama #Colored Text
from colorama import Fore, Back, Style #Colored Text - REMOVE IF YOU HAVE ISSUES WITH OTHER SOFTWARE THAN SPYDER. Remove any Fore, and Style variable if presenting issues!


#Paper, Rock, and Scissors by Miguel Angel Garces Lenis (Python Competition Winnner)
#Build 5 (FINAL)


#POINTS
userPoints = 0
aiPoints = 0

print('')
print(Fore.YELLOW + Style.BRIGHT + "Loading Messages....")
time.sleep(1.5) #Time delay (1.5 seconds)
print(Fore.YELLOW + Style.BRIGHT + "Loading Points....")
time.sleep(1.5)
print(Fore.YELLOW + Style.BRIGHT + "Loading AI actions....")
time.sleep(1.5)
print(Fore.YELLOW + Style.BRIGHT + "Loading User actions....")
time.sleep(1.5)
print(Fore.GREEN + Style.BRIGHT + "LOADING COMPLETED!")
time.sleep(2)

print('')
print('')
print('')
print('')
print('')
print('')

print(Fore.CYAN + Style.BRIGHT +'                               ROCK, PAPER, AND SCISSORS                                  ')
print(Fore.GREEN + Style.BRIGHT +"                                 By Miguel Garces Lenis")
print('')
time.sleep(2)
print(Style.RESET_ALL + "➤ AI: Hello there! My name is IA and we are going to play Paper, Rock, and Scissors!")
time.sleep(3)

userName = input("➤ AI: In order to start playing, you must type a username (Must have more than {}{}3 {}characters): ".format(Fore.GREEN,Style.BRIGHT,Style.RESET_ALL))

while len(userName) < 3 or userName == 'AI': #Checking if userName has more than 3 characters and it is not equal to AI
        print('')
        print('GAME: {}{} {}cannot be used because it belongs to your opponent or it is less than {}{}3 {}characters!'.format(Fore.RED + Style.BRIGHT, userName, Style.RESET_ALL,Fore.GREEN,Style.BRIGHT,Style.RESET_ALL))
        userName = input("➤ AI: You must pass the requirement. Type a username with more than {}{}3 {}characters: ".format(Fore.GREEN,Style.BRIGHT,Style.RESET_ALL))
else:
    print('')

print(Fore.RED + Style.BRIGHT + "SYSTEM: {}Adding {}{} {}to the game....".format(Style.RESET_ALL,Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL))
time.sleep(1)
print(Fore.RED + Style.BRIGHT + "SYSTEM: {}{}{} has successfully registered to the game!".format(Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL))
time.sleep(1)
print('')
print(Style.RESET_ALL + "➤ AI: Alright {}{}{}, let me explain you how to play!".format(Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL))
time.sleep(2)
print("➤ AI: It's pretty simple {}{}{}, you only have to type paper, rock, or scissors!".format(Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL))
time.sleep(2)
print("➤ AI: Then, I will randomly pick one of those three. By the way, I am the BEST in this game!")
time.sleep(2)
print("➤ AI: Anyways, after we both pick rock, paper, or scissors. We will see who the winner is. Rock beats scissors, paper beats rock, and scissors beat paper.")
time.sleep(2)
print("➤ AI: The winner will get one point and the loser will lose a point. In addition, a tied round means two points for both of us. That's all you need to know. All I got to say now is good luck, {}{}{}!".format(Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL))
print('')
time.sleep(3)

def loadingGame(): #You can remove this if you want to.
    print('')
    symbol = '|' * 5
    print("{}{}{}LOADING GAME{}{}".format(Fore.CYAN + Style.BRIGHT,symbol,Style.RESET_ALL,Fore.CYAN + Style.BRIGHT,symbol,))
    print('')

loadingGame()
time.sleep(2)



while True: #From here, the real game starts!

    userAction = input(Style.RESET_ALL + "GAME: {}{}{}, what is your choice? (Rock, Paper, Scissors): ".format(Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL)) #User choice
    print('')
    
    while userAction.lower() not in ("rock", "paper", "scissors"): #If userAction is not equal to rock, paper, or scissors, then, it will ask the user to do it again
        print('GAME: {}{} {}is not a valid option. Please, follow the rules!'.format(Fore.RED + Style.BRIGHT, userAction, Style.RESET_ALL))
        time.sleep(1)
        userAction = input("GAME: {}TRY AGAIN! {}What is your choice? (Rock, Paper, Scissors): ".format(Fore.RED + Style.BRIGHT,(Style.RESET_ALL)))     

    else:  
        ai_actions = ["Rock", "Paper", "Scissors"] #AI choices - If you are adding or removing any actions, do NOT forget to change the conditions!
        ai_choice = random.choice(ai_actions) #AI random choice
        time.sleep(1)
    
        print('')
    
    print(Fore.YELLOW + Style.BRIGHT + "                     ✫ PRE-RESULT ✫       ") #It means that it will show the user and AI choice
    print(Style.RESET_ALL + "GAME: The player {}{} {}chose {}{} {}and AI chose {}{}.".format(Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL,Fore.CYAN + Style.BRIGHT,userAction,Style.RESET_ALL,Fore.CYAN + Style.BRIGHT,ai_choice))
    time.sleep(1)
    
    print('')
    
    #Tied games are giving the user and AI double points
    #From here, the program is checking who is the winner
    
    if userAction.lower() == ai_choice.lower():
        
        userPoints = userPoints + 2  
        aiPoints = aiPoints + 2
    
        print(Fore.BLUE + Style.BRIGHT + "         AND THE WINNER IS..UH?...Looks like we have a tie!              ")
        time.sleep(1)
        print(Style.RESET_ALL + "GAME: {}{} {}and AI chose {}{} {}which took them to a TIE game!".format(Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL,Fore.YELLOW + Style.BRIGHT,userAction,Style.RESET_ALL))
        print('GAME: Both players got {}+2 points {}for tied results!'.format(Fore.GREEN + Style.BRIGHT,(Style.RESET_ALL)))
        print('')
        print(Style.RESET_ALL + 'You won:{} +2 Point'.format(Fore.GREEN + Style.BRIGHT)) #Scoreboard for round tied - You will see this on every round even if you win or lose.
        print(Style.RESET_ALL + 'AI lost:{} +2 Points'.format(Fore.GREEN + Style.BRIGHT))
        print(Style.RESET_ALL + userName +"'s Total Points:{} {}".format(Fore.YELLOW + Style.BRIGHT,(userPoints)))
        print(Style.RESET_ALL + 'AI Total Points:{} {}'.format(Fore.YELLOW + Style.BRIGHT,(aiPoints)))
        
        print('')
        time.sleep(1)
    elif userAction.lower() == "rock":
        if ai_choice.lower() == "scissors":
            
            userPoints = userPoints + 1
            aiPoints = aiPoints - 1
            
            print(Fore.GREEN + Style.BRIGHT +"{} WON THIS ROUND!".format(userName))
            print(Style.RESET_ALL + "GAME: {}{}'s {}{} {}was to heavy and broke AI's{} {}!".format(Fore.CYAN + Style.BRIGHT,userName,Fore.YELLOW + Style.BRIGHT,userAction,Style.RESET_ALL,Fore.YELLOW + Style.BRIGHT,ai_choice))
            
            print('')
            
            print(Style.RESET_ALL + 'You won:{} +1 Point'.format(Fore.GREEN + Style.BRIGHT))
            print(Style.RESET_ALL + 'AI lost:{} -1 Points'.format(Fore.RED + Style.BRIGHT))
            print(Style.RESET_ALL + userName +"'s Total Points:{} {}".format(Fore.YELLOW + Style.BRIGHT,(userPoints)))
            print(Style.RESET_ALL + 'AI Total Points:{} {}'.format(Fore.YELLOW + Style.BRIGHT,(aiPoints)))
            time.sleep(1)     
            print('')
        else:
            
            userPoints = userPoints - 1
            aiPoints = aiPoints + 1
            
            print(Fore.RED + Style.BRIGHT + "AI AGGRESSIVELY COVERED YOU! (No, not to protect you)                 ")
            print(Style.RESET_ALL + "GAME: AI's {}{} {}covered your {}{}!".format(Fore.YELLOW + Style.BRIGHT,ai_choice,Style.RESET_ALL,Fore.YELLOW + Style.BRIGHT,userAction))
            
            print('')
            
            print(Style.RESET_ALL + 'You lost:{} -1 Point'.format(Fore.RED + Style.BRIGHT))
            print(Style.RESET_ALL + 'AI won:{} +1 Points'.format(Fore.GREEN + Style.BRIGHT))
            print(Style.RESET_ALL + userName +"'s Total Points:{} {}".format(Fore.YELLOW + Style.BRIGHT,(userPoints)))
            print(Style.RESET_ALL + 'AI Total Points:{} {}'.format(Fore.YELLOW + Style.BRIGHT,(aiPoints)))
            
    elif userAction.lower() == "paper":
        if ai_choice.lower() == "rock":
            
            userPoints = userPoints + 1
            aiPoints = aiPoints - 1
            
            print(Fore.GREEN + Style.BRIGHT +"{} WRAPPED AI's SELECTION!".format(userName))
            print(Style.RESET_ALL + "GAME: {}{}'s {}{} {}took AI's {}{} {}and wrapped it like a gift!".format(Fore.CYAN + Style.BRIGHT,userName,Fore.YELLOW + Style.BRIGHT,userAction,Style.RESET_ALL,Fore.YELLOW + Style.BRIGHT,ai_choice,Style.RESET_ALL))
            
            print('')
            
            print(Style.RESET_ALL + 'You won:{} +1 Point'.format(Fore.GREEN + Style.BRIGHT))
            print(Style.RESET_ALL + 'AI lost:{} -1 Points'.format(Fore.RED + Style.BRIGHT))
            print(Style.RESET_ALL + userName +"'s Total Points:{} {}".format(Fore.YELLOW + Style.BRIGHT,(userPoints)))
            print(Style.RESET_ALL + 'AI Total Points:{} {}'.format(Fore.YELLOW + Style.BRIGHT,(aiPoints)))
            time.sleep(1)     
            print('')
        else:
             
            userPoints = userPoints - 1
            aiPoints = aiPoints + 1
            
            print(Fore.RED + Style.BRIGHT + "HOLY COW! AI JUST CUT YOUR PAPER IN HALF!")
            print(Style.RESET_ALL + "GAME: Yes, paper cuts are real, but AI's {}{} {}could cut a tree down like it did with {}{}'s {}{}!".format(Fore.YELLOW + Style.BRIGHT,ai_choice,Style.RESET_ALL,Fore.CYAN + Style.BRIGHT,userName,Fore.YELLOW + Style.BRIGHT,userAction))
            
            print('')
            
            print(Style.RESET_ALL + 'You lost:{} -1 Point'.format(Fore.RED + Style.BRIGHT))
            print(Style.RESET_ALL + 'AI won:{} +1 Points'.format(Fore.GREEN + Style.BRIGHT))
            print(Style.RESET_ALL + userName +"'s Total Points:{} {}".format(Fore.YELLOW + Style.BRIGHT,(userPoints)))
            print(Style.RESET_ALL + 'AI Total Points:{} {}'.format(Fore.YELLOW + Style.BRIGHT,(aiPoints)))
            
    elif userAction.lower() == "scissors":
        if ai_choice.lower() == "paper":
            
            userPoints = userPoints + 1
            aiPoints = aiPoints - 1
            
            print(Fore.GREEN + Style.BRIGHT +"{} JUST CUT AI's RECORD!".format(userName))
            print(Style.RESET_ALL + "GAME: What's better than cutting someone's record? Well, {}{}'s {}{} {}to cut AI's {}{}".format(Fore.CYAN + Style.BRIGHT,userName,Fore.YELLOW + Style.BRIGHT,userAction,Style.RESET_ALL,Fore.YELLOW + Style.BRIGHT,ai_choice))
            
            print('')
            
            print(Style.RESET_ALL + 'You won:{} +1 Point'.format(Fore.GREEN + Style.BRIGHT))
            print(Style.RESET_ALL + 'AI lost:{} -1 Points'.format(Fore.RED + Style.BRIGHT))
            print(Style.RESET_ALL + userName +"'s Total Points:{} {}".format(Fore.YELLOW + Style.BRIGHT,(userPoints)))
            print(Style.RESET_ALL + 'AI Total Points:{} {}'.format(Fore.YELLOW + Style.BRIGHT,(aiPoints)))
            time.sleep(1)     
            print('')
        else:
            
            userPoints = userPoints - 1
            aiPoints = aiPoints + 1
            
            print(Fore.RED + Style.BRIGHT + "AI WENT INSANE MODE ON YOU AND BROKE YOUR SCISSORS! (No hard feelings!)           ")
            print(Style.RESET_ALL + "GAME: AI was not thinking twice and broke {}{}'s {}{}{}!".format(Fore.CYAN + Style.BRIGHT,userName,Fore.YELLOW + Style.BRIGHT,userAction,Style.RESET_ALL))
            
            print('')
            
            print(Style.RESET_ALL + 'You lost:{} -1 Point'.format(Fore.RED + Style.BRIGHT))
            print(Style.RESET_ALL + 'AI won:{} +1 Points'.format(Fore.GREEN + Style.BRIGHT))
            print(Style.RESET_ALL + userName +"'s Total Points:{} {}".format(Fore.YELLOW + Style.BRIGHT,(userPoints)))
            print(Style.RESET_ALL + 'AI Total Points:{} {}'.format(Fore.YELLOW + Style.BRIGHT,(aiPoints)))     
            
    play_again = input(Style.RESET_ALL +"GAME: Would you like to continue? (y/n): ") #Of course, do you want to play again?
    while play_again.lower() not in ("y", "n", "yes", "no"): #Wrong input
        play_again = input(Style.BRIGHT + Fore.RED +"TRY AGAIN! {}Would you like to continue playing? (y/n): ".format(Style.RESET_ALL)) 
    if play_again.lower() == 'n' or play_again.lower() == 'no': #From here, the program will pick the winner of the game
        if userPoints > aiPoints: #WIN      
            print('')
            print(Fore.BLUE + Style.BRIGHT + "✻ WINNER ✻     ")
            time.sleep(2)
            print(Fore.GREEN + Style.BRIGHT + "   {}".format(userName))      
            print('')
            time.sleep(2) 
            print(Style.RESET_ALL + "➤ AI: Oh Wow {}{}{}! You are actually a strong opponent!".format(Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL))
            time.sleep(2)
            print("➤ AI: But don't get too comfortable. One day, I will beat you because I am the BEST in this game (At least, that's what my programmer told me)")
            time.sleep(2)
            print("➤ AI: Anyways, no hard feelings! I just hope you had a great time playing with me and I hope you have a wonderful day!")
            time.sleep(2)
            print("➤ AI: We'll see each other again on another game. Goodbye!") 
            time.sleep(4)
            print('')
            print(Fore.YELLOW + Style.BRIGHT + '======= FINAL SCORE ======= ') #Final results of the game (TIED games have different colors but it is the same scoreboard)
            print(Style.RESET_ALL + "{}'s Score: {}{}".format(userName,Fore.GREEN + Style.BRIGHT,userPoints))
            print(Style.RESET_ALL + "AI's Score: {}{}".format(Fore.RED + Style.BRIGHT,aiPoints))
            break        
            
        if userPoints < aiPoints:   #DEFEAT
            print('')
            print(Fore.BLUE + Style.BRIGHT + "✻ WINNER ✻     ")
            time.sleep(2)
            print(Fore.GREEN + Style.BRIGHT + "     AI")     
            print('')
            time.sleep(2)    
            print(Style.RESET_ALL + "➤ AI: I WON! I am actually not impressed at all... I am the best player in this game!")
            time.sleep(2)
            print(Style.RESET_ALL + "➤ AI: I cannot lie, you did good, but not enough to beat me!")
            time.sleep(2)
            print(Style.RESET_ALL + "➤ AI: Hey {}{}{}, do not give up, just keep pushing and practice and you might beat me and yes, I am challenging you!".format(Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL))
            time.sleep(2)
            print(Style.RESET_ALL + "➤ AI: It was good playing with you and I had a lot of fun, I hope you did too.")
            time.sleep(2)
            print(Style.RESET_ALL + "➤ AI: Anyways, we will see each other again on another game. See you, {}{}".format(Fore.CYAN + Style.BRIGHT,userName))   
            time.sleep(4)
            print("")
            print(Fore.YELLOW + Style.BRIGHT + '======= FINAL SCORE ======= ')
            print(Style.RESET_ALL + "{}'s Score: {}{}".format(userName,Fore.GREEN + Style.BRIGHT,userPoints))
            print(Style.RESET_ALL + "AI's Score: {}{}".format(Fore.GREEN + Style.BRIGHT,aiPoints))
            break        
        else: #TIED MESSAGE
            print('')
            print(Fore.BLUE + Style.BRIGHT + "✻ WINNER ✻     ")
            time.sleep(2)
            print(Fore.GREEN + Style.BRIGHT + "{}{} {}and {}AI!".format(Fore.GREEN + Style.BRIGHT,userName,Style.RESET_ALL,Fore.GREEN + Style.BRIGHT))
            print('')
            time.sleep(2)
            print(Style.RESET_ALL + "➤ AI: Incredible {}{}{}! We actually managed to get a tied game!".format(Fore.CYAN + Style.BRIGHT,userName,Style.RESET_ALL))
            time.sleep(2)
            print("➤ AI: I will not lie to you, you almost burn my whole software and hardware. I was not thinking about a tied game.")
            time.sleep(2)
            print("➤ AI: We cannot just leave it right here, right?")   
            print('')
            time.sleep(2)           
            play_again = input(Style.RESET_ALL +"AI: Would you like to rematch? (y/n): ") #Option to rematch if game result is TIED -REMOVE this line if you don't want to rematch when game is TIED and fix the text for the other lines
            while play_again.lower() not in ("y", "n", "yes", "no"):
                play_again = input(Style.BRIGHT + Fore.RED +"TRY AGAIN {}AI: Would you like to rematch? (y/n): ".format(Style.RESET_ALL)) #-REMOVE this line if you don't want to rematch when game is TIED and fix the text for the other lines
                
            if play_again.lower() == 'n' or play_again.lower() == "no":          #-REMOVE this line if you don't want to rematch when game is TIED          and fix the text for the other lines
                time.sleep(2)
                print("➤ AI: I thought we could have a rematch to define the real winner, but I guess we are tired.") 
                time.sleep(2)
                print("➤ AI: It was fun playing with you, honestly, I never had a lot of fun before.") 
                time.sleep(2)
                print("➤ AI: Remember, if you want to beat me, I'm always here waiting for you >:)")
                time.sleep(2)
                print("➤ AI: I'll be waiting for you, {}{}".format(Fore.CYAN + Style.BRIGHT,userName)) 
                time.sleep(4)
                print('')
                print(Fore.YELLOW + Style.BRIGHT + '======= FINAL SCORE ======= ')
                print(Style.RESET_ALL + "{}'s Score: {}{}".format(userName,Fore.BLUE + Style.BRIGHT,userPoints))
                print(Style.RESET_ALL + "AI's Score: {}{}".format(Fore.BLUE + Style.BRIGHT,aiPoints))