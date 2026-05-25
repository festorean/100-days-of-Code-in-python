import random
import os
import art

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def deal_card():
    """Return random card from the deck."""
    card = random.choice(cards)
    return card


def calculate_score(hand):
    """Calculate score of user and computer."""
    score = sum(hand)

    #Blackjack
    if score == 21 and len(hand) == 2:
        return 0
    #check fo ace
    while 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def compare(user_score, computer_score):
    """Compare user and computer."""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer has a blackjack. You lose"
    elif user_score == 0:
        return "You have a blackjack. You win"
    elif user_score > 21:
        return "You lose"
    elif computer_score > 21:
        return "You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_card = []

    computer_card = []

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    game_over = False
    while not game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your cards: {user_card}, score: {user_score}")
        print(f"Computer first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_draw = input("do you want to add another card? y/n: ").lower
            if should_draw == "y":
                user_card.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())

        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
    print("\n --- Final Result ---")
    print(f"Your cards: {user_card}, score: {user_score}")
    print(f"Computer cards: {computer_card}, score: {computer_score}")
    print(compare(user_score, computer_score))

while True:
    play = input("Do you want to play Blackjack ? y/n: ").lower()
    if play == "y":
        clear()
        play_game()
    else:
        break