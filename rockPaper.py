import random
import time
import os

rock = 1
paper = 2
scissors = 3
name = {rock: "Rock", paper: 'Paper', scissors: 'Scissors'}
rule = {rock: scissors, paper: rock , scissors : paper}
player_score = 0
computer_score = 0


def computerChoice():
    return random.randint(1, 3)


def score():
    global player_score, computer_score
    print("----Score---")
    print("Player : ", player_score)
    print("Computer : ", computer_score)


def game():
    user_choice = userInput()
    computer_choice = computerChoice()
    result(user_choice, computer_choice)
    return play_again()


def userInput():
    print("Number")
    print("1 : Rock")
    print("2 : Paper")
    print("2 : Scissor")
    while True:
        try:
            choice = int(input("Enter yout Choice-- "))
            if choice in {1, 2, 3}:
                return choice
            else:
                raise ValueError
        except ValueError as error:
            print("Please enter the number {1, 2, 3}")


def result(user_choice, computer_choice):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print('3...')
    time.sleep(1)
    print("Coputer Choice {0}".format(name[computer_choice]))
    global player_score, computer_score
    if computer_choice == user_choice:
        print("---Tie game---")
    else:
        if rule[user_choice] == computer_choice:
            print("You won this round")
            player_score += 1
        else:
            print("Computer Won ")
            computer_score += 1


def play_again():
    answer = input("Would you like to play it again : --- y/n : ")
    if answer in {'yes', 'y', 'Y'}:
        os.system("CLS")
        return answer
    else:
        print("----Thank you For Playing the game----")


def start():
    print("-----ROCK-----PAPER-----SCISSOR-----")
    print("_____________________________________")
    print("       ____________________          ")
    while game():
        pass
    score()


if __name__ == '__main__':
    start()
