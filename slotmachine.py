import random

# List of possible symbols
symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"]

def spin_slot_machine():
    # Randomly choose a symbol for each slot
    slot1 = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)

    return slot1, slot2, slot3

def check_win(slots):
    # Check if all three slots have the same symbol
    return slots[0] == slots[1] == slots[2]

def play_slot_machine():
    input("Press Enter to spin the slot machine!")
    slots = spin_slot_machine()
    print("Slot machine shows:", slots)

    if check_win(slots):
        print("Congratulations! You won!")
    else:
        print("Sorry, try again.")

# Start the game
play_slot_machine()
