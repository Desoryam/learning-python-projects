#                                                                 rock paper scissors game
from random import choice as c

l=["rock","paper","scissor"]
player_score=0
bot_score=0
while True:
    print()
    print("welcome to the game  of rock paper scissors".upper().center(50,"*"))
    print("1. START THE GAME\n2. EXIT")
    ch=int(input("Enter your choice: "))
    if ch==1:
        ro=int(input("Enter the number of rounds you want to play: "))
        print()
        for i in range(ro):
            print(f"Round {i+1}")
            print("pick one: rock, paper, scissor")
            u=input("Enter your choice: ").lower()
            print()
            bot=c(l)
            if u in l:
                if u==bot:
                    print(("you have a draw\n".upper()).center(50))
                    print(f"the bot chose \"{bot}\" and you chose \"{u}\"\n")
                elif u==l[0] and bot==l[2] or u==l[1] and bot==l[0] or u==l[2] and bot==l[1]:
                    print(("you win the round\n".upper()).center(50))
                    player_score+=1
                    print(f"the bot chose \"{bot}\" and you chose \"{u}\"\n")

                elif u==l[0] and bot==l[1] or u==l[1] and bot==l[2] or u==l[2] and bot==l[0]:
                    print(("you lose the round\n".upper()).center(50))
                    bot_score+=1
                    print(f"the bot chose \"{bot}\" and you chose \"{u}\"\n")
            else:
                print("invalid choice")
                break
        if player_score>bot_score:
            print(("you win the game\n".upper()).center(50))
            print(f"your score is {player_score} and the bot's score is {bot_score}\n")
        elif player_score<bot_score:
            print(("you lose the game\n".upper()).center(50))
            print(f"your score is {player_score} and the bot's score is {bot_score}\n")
        else:
            print(("the game is a draw\n".upper()).center(50))
            print(f"your score is {player_score} and the bot's score is {bot_score}\n")

    elif ch==2:
        print("\nthank you for playing the game")
        break
    else:
        print("invalid choice")
