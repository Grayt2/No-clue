import random

def rockPaperScissors(yourplay):
    yourplay = input('what is your move [Rock, paper or scissors]: ')
    plays = ['Rock', 'paper', 'scissors']
    robotguess = plays[random.randrange(1,3)]
    if robotguess == yourplay:
        rockPaperScissors(0)
    if yourplay == "Rock" and robotguess == "paper" or yourplay == "paper" and robotguess == "scissors" or yourplay == "scissors" and robotguess == "Rock":
        return "you lose!"
    else:
        return "you win"

print(rockPaperScissors(0))
