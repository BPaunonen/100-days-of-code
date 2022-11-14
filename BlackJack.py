import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack."
    elif user_score > 21:
        return "You went over 21, you lose."
    elif computer_score > 21:
        return "Opponent went over 21, you win."
    elif user_score > computer_score:
        return "You scored higher, you win."
    else: 
        return "Opponent scored higher, you lose."

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are :{user_cards} and your total is {user_score}.\n")
        print(f"Computer's first card is: {computer_cards[0]}\n")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_deal = input("Type 'y' to draw another coard or 'n' to pass. \n")
            if user_deal == "y" or user_deal == "Y":
                user_cards.append(deal_card())
            else: 
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand was {user_cards} with a total of {user_score}.\n")
    print(f"The opponents final hand was {computer_cards} with a total of {computer_score}.\n")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack, 'y' or 'n'?") == "y":
    os.system('clear')
    play_game()

