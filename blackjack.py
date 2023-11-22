import random


def create_deck():
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    deck = [f"{value}_of_{suit}" for value in values for suit in suits]
    random.shuffle(deck)
    return deck


def deal_card(hand, deck):
    card = deck.pop()
    hand.append(card)
    return card


def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        card_value, _ = card.split('_of_')
        if card_value in ["jack", "queen", "king"]:
            value += 10
        elif card_value == "ace":
            ace_count += 1
            value += 11
        else:
            value += int(card_value)

    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1

    return value


def check_win(dealer_value, player_value):
    if dealer_value > 21 or player_value > dealer_value:
        return 1
    elif dealer_value > player_value:
        return -1
    else:
        return 0
