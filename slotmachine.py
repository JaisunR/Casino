import random

# List of possible symbols
symbols = ["Cherry", "7", "Banana", "Watermelon", "Bell"]


def spin_slot_machine():
    # Randomly choose a symbol for each slot
    slot1 = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)

    return slot1, slot2, slot3


def check_win(slots):
    # Check if all three slots have the same symbol
    return slots[0] == slots[1] == slots[2]