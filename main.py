import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from PIL import Image, ImageTk
import slotmachine
import blackjack


class CasinoGui:
    def __init__(self, root):
        # Create initial window
        self.root = root
        self.root.title("Casino")
        self.root.geometry("600x400")
        self.create_login()
        self.balance = 0

    def create_login(self):
        # Title
        self.title_label = ctk.CTkLabel(self.root, text="Welcome to the Casino!", font=("Arial", 40, "bold", "italic"))
        self.title_label.pack(pady=50)

        # Login and Password frame
        self.pass_log_frame = ttk.Frame(self.root)
        self.pass_log_frame.pack(pady=10)

        # Login Entry
        self.login_label = ctk.CTkLabel(self.pass_log_frame, text="Login ID:", font=('Arial', 20))
        self.login_label.grid(row=0, column=0)
        self.login_entry = ctk.CTkEntry(self.pass_log_frame, width=200)
        self.login_entry.grid(row=0, column=1)

        # Password Entry
        self.password_label = ctk.CTkLabel(self.pass_log_frame, text="Password:", font=('Arial', 20))
        self.password_label.grid(row=1, column=0)
        self.password_entry = ctk.CTkEntry(self.pass_log_frame, show="*", width=200)
        self.password_entry.grid(row=1, column=1)

        # Login button
        self.button_login = ctk.CTkButton(self.root, text="Login", command=self.login, width=175)
        self.button_login.pack(pady=(25, 5))

        # Register button
        self.button_register = ctk.CTkButton(self.root, text="Register a new account", command=self.register, width=175)
        self.button_register.pack()

    def clear_login(self):
        # Clear the login widgets
        self.title_label.pack_forget()
        self.pass_log_frame.pack_forget()
        self.button_login.pack_forget()
        self.button_register.pack_forget()

    def login(self):
        # Get login and password from user
        login_id = self.login_entry.get()
        password = self.password_entry.get()

        # Take user to casino menu if credentials verified
        self.casino_menu()

    def casino_menu(self):
        # Clear login page
        self.clear_login()

        # Casino Menu Title
        self.menu_title_label = ctk.CTkLabel(self.root, text="Casino Menu", font=("Arial", 35, "bold"))
        self.menu_title_label.pack(pady=35)

        # Play Button
        self.play_button = ctk.CTkButton(self.root, text="Play", font=("Arial", 15, "bold"),
                                         command=self.play, width=250, height=50)
        self.play_button.pack()

        # Deposit & Withdraw Button
        self.money_button = ctk.CTkButton(self.root, text="Deposit & Withdraw", font=("Arial", 15, "bold"),
                                          command=self.deposit_withdraw, width=250, height=50)
        self.money_button.pack(pady=5)

        # View History Button
        self.history_button = ctk.CTkButton(self.root, text="View History", font=("Arial", 15, "bold"),
                                            command=self.view_history, width=250, height=50)
        self.history_button.pack()

        # Logout Button
        self.logout_button = ctk.CTkButton(self.root, text="Logout", font=("Arial", 15, "bold"),
                                           command=self.logout, width=250, height=50)
        self.logout_button.pack(pady=5)

    def clear_menu(self):
        # Clear casino menu
        self.menu_title_label.pack_forget()
        self.play_button.pack_forget()
        self.money_button.pack_forget()
        self.history_button.pack_forget()
        self.logout_button.pack_forget()

    def play(self):
        # Get rid of menu
        self.clear_menu()

        # Play screen title
        self.play_title_label = ctk.CTkLabel(self.root, text="Choose a Game", font=("Arial", 35, "bold"))
        self.play_title_label.pack(pady=35)

        # Play slots button
        self.play_slots_button = ctk.CTkButton(self.root, text="Slots", command=self.slots_play,
                                               font=("Arial", 15, "bold"),
                                               width=250, height=50)
        self.play_slots_button.pack()

        # Play Blackjack button
        self.play_blackjack_button = ctk.CTkButton(self.root, text="Blackjack", font=("Arial", 15, "bold"),
                                                   command=self.blackjack_play,
                                                   width=250, height=50)
        self.play_blackjack_button.pack(pady=5)

        # Go back button
        self.back_play_button = ctk.CTkButton(self.root, text="Back", font=("Arial", 15, "bold"),
                                              command=self.back_play,
                                              width=250, height=50)
        self.back_play_button.pack()

    def slots_play(self):
        # Clear play screen
        self.back_play_button.pack_forget()
        self.play_title_label.pack_forget()
        self.play_slots_button.pack_forget()
        self.play_blackjack_button.pack_forget()

        # If Windows use 175,175
        # Size of Images
        new_size = (125, 125)

        # Load and resize slot machine images into variables
        self.img7 = ImageTk.PhotoImage(Image.open("Slots Symbols/7.png").resize(new_size))
        self.imgCherry = ImageTk.PhotoImage(Image.open("Slots Symbols/Cherry.png").resize(new_size))
        self.imgBell = ImageTk.PhotoImage(Image.open("Slots Symbols/Bell.png").resize(new_size))
        self.imgWatermelon = ImageTk.PhotoImage(Image.open("Slots Symbols/Watermelon.png").resize(new_size))
        self.imgBanana = ImageTk.PhotoImage(Image.open("Slots Symbols/Banana.png").resize(new_size))

        # Slots title
        self.title_label = ctk.CTkLabel(self.root, text="Slots!", font=("Arial", 30, "bold", "italic"))
        self.title_label.pack(pady=25)

        # Frame holding 3 slot images intialized with cherries
        self.img_frame = tk.Frame(self.root)
        self.img_frame.pack(pady=(0, 20))

        # 1st Image
        self.img_1 = tk.Label(self.img_frame, image=self.imgCherry)
        self.img_1.grid(row=0, column=0)

        # 2nd Image
        self.img_2 = tk.Label(self.img_frame, image=self.imgCherry)
        self.img_2.grid(row=0, column=1)

        # 3rd Image
        self.img_3 = tk.Label(self.img_frame, image=self.imgCherry)
        self.img_3.grid(row=0, column=2)

        # Spin button
        self.spin_button = ctk.CTkButton(self.root, text="Spin", font=("Arial", 15, "bold"),
                                         command=self.slots_spin, width=75, height=30)
        self.spin_button.pack(pady=(0, 10))

        # Frame holding account balance and bet amount
        self.bet_frame = ttk.Frame(self.root)
        self.bet_frame.pack(pady=5)

        # Label Balance:
        self.account_label = ctk.CTkLabel(self.bet_frame, text="Balance:", font=("Arial", 15))
        self.account_label.grid(row=0, column=0)

        # Balance amount
        self.balance_label = ctk.CTkLabel(self.bet_frame, text=f"${self.balance:.2f}", font=("Arial", 20, "bold"),
                                          text_color='green')
        self.balance_label.grid(row=0, column=1)

        # Label Amount:
        self.amount_label = ctk.CTkLabel(self.bet_frame, text="Amount:", font=("Arial", 15))
        self.amount_label.grid(row=0, column=2, padx=(40, 5))

        # Entry field for bet amount
        self.bet_entry = ctk.CTkEntry(self.bet_frame)
        self.bet_entry.grid(row=0, column=3, padx=(0, 5))

        # Go back button
        self.back_button = ctk.CTkButton(self.root, text="Back", font=("Arial", 15, "bold"),
                                         command=self.slots_back,
                                         width=250, height=50)
        self.back_button.pack(pady=(20, 0))

    def slots_spin(self):
        # Instantiate slotmachine
        slots = slotmachine

        try:
            # Get amount from entry field
            amount = float(self.bet_entry.get())
            # Error handling for negatives and zero amounts
            if amount <= 0:
                messagebox.showerror("Casino Error", "Amount must be greater than zero")
            # Correct Entry
            elif amount <= self.balance:
                # Subtract amount from balance and update balance label
                self.balance -= amount
                self.update_balance_label()
                # Add spin machine results to array
                result = slots.spin_slot_machine()
                # Configure images based on result
                self.img_1.configure(image=self.get_image_for_symbol(result[0]))
                self.img_2.configure(image=self.get_image_for_symbol(result[1]))
                self.img_3.configure(image=self.get_image_for_symbol(result[2]))
                # If all 3 slots match 10x amount bet
                if slots.check_win(result):
                    self.balance += amount * 10
                    self.update_balance_label()
            # Error handling for Insufficient Balance
            elif amount > self.balance:
                messagebox.showerror("Casino Error", "Insufficient Funds")
            # Error handling for non numbers
            else:
                messagebox.showerror("Casino Error", "Invalid Character")
        except:
            messagebox.showerror("Casino Error", "Invalid Character")

    def get_image_for_symbol(self, symbol):
        # Return image based on word
        if symbol == "Cherry":
            return self.imgCherry
        elif symbol == "7":
            return self.img7
        elif symbol == "Banana":
            return self.imgBanana
        elif symbol == "Watermelon":
            return self.imgWatermelon
        elif symbol == "Bell":
            return self.imgBell

    def slots_back(self):
        # Clears slots screen
        self.title_label.pack_forget()
        self.back_button.pack_forget()
        self.img_frame.pack_forget()
        self.spin_button.pack_forget()
        self.bet_frame.pack_forget()

        # Creates play screen
        self.play()

    def blackjack_play(self):
        # Clear play screen
        self.back_play_button.pack_forget()
        self.play_title_label.pack_forget()
        self.play_slots_button.pack_forget()
        self.play_blackjack_button.pack_forget()

        # Blackjack title
        self.title_label = ctk.CTkLabel(self.root, text="Blackjack!", font=("Arial", 30, "bold", "italic"))
        self.title_label.pack(pady=25)

        # Frame holding card images
        self.card_frame = ttk.Frame(self.root)
        self.card_frame.pack()

        # Frame for your and dealer label with values
        self.value_frame = tk.Frame(self.root)
        self.value_frame.pack()
        # Your label
        self.your_value = 0
        self.your = ctk.CTkLabel(self.value_frame, text=f"Your: {self.your_value}", font=("Arial", 15, "bold"))
        self.your.grid(row=0, column=0, padx=(0, 300))
        # Dealer label
        self.dealer_value = 0
        self.dealer = ctk.CTkLabel(self.value_frame, text=f"Dealer: {self.your_value}", font=("Arial", 15, "bold"))
        self.dealer.grid(row=0, column=1)

        # Load images for deck of cards
        self.load_card_images()
        # Create default card image
        default_size = (65, 100)
        self.card_default = ImageTk.PhotoImage(Image.open("Deck of Cards/card back red.png").resize(default_size))

        # User cards
        self.uCard1 = tk.Label(self.card_frame, image=self.card_default)
        self.uCard1.grid(row=0, column=0)
        self.uCard2 = tk.Label(self.card_frame, image=self.card_default)
        self.uCard2.grid(row=0, column=1)
        self.uCard3 = tk.Label(self.card_frame, image=self.card_default)
        self.uCard3.grid(row=0, column=2)
        self.uCard4 = tk.Label(self.card_frame, image=self.card_default)
        self.uCard4.grid(row=0, column=3, padx=(0, 20))

        # Dealer cards
        self.dCard1 = tk.Label(self.card_frame, image=self.card_default)
        self.dCard1.grid(row=0, column=4)
        self.dCard2 = tk.Label(self.card_frame, image=self.card_default)
        self.dCard2.grid(row=0, column=5)
        self.dCard3 = tk.Label(self.card_frame, image=self.card_default)
        self.dCard3.grid(row=0, column=6)
        self.dCard4 = tk.Label(self.card_frame, image=self.card_default)
        self.dCard4.grid(row=0, column=7)

        # Frame holding hit and stand buttons
        self.hs_frame = ttk.Frame(self.root)
        self.hs_frame.pack(pady=5)

        # Hit button
        self.bet_button = ctk.CTkButton(self.hs_frame, text="Hit", font=("Arial", 15, "bold"),
                                        width=60, height=30)
        self.bet_button.grid(row=0, column=1, padx=(0, 5))

        # Stand button
        self.bet_button = ctk.CTkButton(self.hs_frame, text="Stand", font=("Arial", 15, "bold"),
                                        width=60, height=30)
        self.bet_button.grid(row=0, column=2)

        # Frame holding account balance and bet amount
        self.bet_frame = ttk.Frame(self.root)
        self.bet_frame.pack(pady=5)

        # Label Balance:
        self.account_label = ctk.CTkLabel(self.bet_frame, text="Balance:", font=("Arial", 15))
        self.account_label.grid(row=0, column=0)

        # Balance amount
        self.balance_label = ctk.CTkLabel(self.bet_frame, text=f"${self.balance:.2f}", font=("Arial", 20, "bold"),
                                          text_color='green')
        self.balance_label.grid(row=0, column=1)

        # Label Amount:
        self.amount_label = ctk.CTkLabel(self.bet_frame, text="Amount:", font=("Arial", 15))
        self.amount_label.grid(row=0, column=2, padx=(40, 5))

        # Entry field for bet amount
        self.bet_entry = ctk.CTkEntry(self.bet_frame)
        self.bet_entry.grid(row=0, column=3, padx=(0, 5))

        # Bet button
        self.bet_button = ctk.CTkButton(self.bet_frame, text="Bet", font=("Arial", 15, "bold"),
                                        command=self.blackjack_bet, width=60, height=30)
        self.bet_button.grid(row=0, column=4)

        # Go back button
        self.back_button = ctk.CTkButton(self.root, text="Back", font=("Arial", 15, "bold"),
                                         command=self.blackjack_back,
                                         width=250, height=50)
        self.back_button.pack(pady=(20, 0))

    def blackjack_bet(self):
        try:
            # Get amount from entry field
            amount = float(self.bet_entry.get())
            # Error handling for negatives and zero amounts
            if amount <= 0:
                messagebox.showerror("Casino Error", "Amount must be greater than zero")
            # Correct Entry
            elif amount <= self.balance:
                # Subtract amount from balance and update balance label
                self.balance -= amount
                self.update_balance_label()

                self.player_hand = []
                self.dealer_hand = []

                self.player_value = 0
                self.dealer_value = 0

                self.deck = blackjack.create_deck()

                # self.player_value = blackjack.calculate_hand_value(self.player_hand)

                blackjack.deal_card(self.player_hand, self.deck)
                self.uCard1.configure(image=self.card_images[self.player_hand[0]])

                blackjack.deal_card(self.player_hand, self.deck)
                self.uCard2.configure(image=self.card_images[self.player_hand[1]])

                self.your_value = blackjack.calculate_hand_value(self.player_hand)
                self.your.configure(text=f"Your: {self.your_value}")

                blackjack.deal_card(self.dealer_hand, self.deck)
                self.dCard1.configure(image=self.card_images[self.dealer_hand[0]])

                self.dealer_value = blackjack.calculate_hand_value(self.dealer_hand)
                self.dealer.configure(text=f"Dealer: {self.dealer_value}")

                blackjack.deal_card(self.dealer_hand, self.deck)

                print(self.player_hand)
                print(self.dealer_hand)



            # Error handling for Insufficient Balance
            elif amount > self.balance:
                messagebox.showerror("Casino Error", "Insufficient Funds")
            # Error handling for non numbers
            else:
                messagebox.showerror("Casino Error", "Invalid Character")
        except:
            messagebox.showerror("Casino Error", "Invalid Character")

    def load_card_images(self):
        new_size = (65, 100)
        suits = ["spades", "hearts", "diamonds", "clubs"]
        values = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

        self.card_images = {}
        for suit in suits:
            for value in values:
                card_name = f"{value}_of_{suit}"
                img = Image.open(f"Deck of Cards/{value}_of_{suit}.png").resize(new_size)
                self.card_images[card_name] = ImageTk.PhotoImage(img)

    def blackjack_back(self):
        # Clear blackjack screen
        self.title_label.pack_forget()
        self.back_button.pack_forget()
        self.bet_frame.pack_forget()
        self.hs_frame.pack_forget()
        self.card_frame.pack_forget()
        self.value_frame.pack_forget()

        # Create casino menu
        self.casino_menu()

    def back_play(self):
        # Clear play screen
        self.back_play_button.pack_forget()
        self.play_title_label.pack_forget()
        self.play_slots_button.pack_forget()
        self.play_blackjack_button.pack_forget()

        # Create casino menu
        self.casino_menu()

    def deposit_withdraw(self):
        # Clear menu
        self.clear_menu()

        # Title for Deposit & Withdraw page
        self.dep_title_label = ctk.CTkLabel(self.root, text="Deposit & Withdraw", font=("Arial", 35, "bold"))
        self.dep_title_label.pack(pady=35)

        # Frame holding deposit and withdraw
        self.dep_frame = ttk.Frame(self.root)
        self.dep_frame.pack(pady=5)

        # Label Amount:
        self.amount_label = ctk.CTkLabel(self.dep_frame, text="Amount:", font=("Arial", 15))
        self.amount_label.grid(row=0, column=0)
        # Entry field for deposit amount
        self.dep_entry = ctk.CTkEntry(self.dep_frame)
        self.dep_entry.grid(row=0, column=1)
        # Deposit button
        self.button_login = ctk.CTkButton(self.dep_frame, text="Deposit", command=self.dep_dw, width=5, height=5)
        self.button_login.grid(row=0, column=2)

        # Label Amount:
        self.amount_label = ctk.CTkLabel(self.dep_frame, text="Amount:", font=("Arial", 15))
        self.amount_label.grid(row=3, column=0)
        # Entry field for withdraw amount
        self.with_entry = ctk.CTkEntry(self.dep_frame)
        self.with_entry.grid(row=3, column=1)
        # Withdraw button
        self.button_login = ctk.CTkButton(self.dep_frame, text="Withdraw", command=self.with_dw, width=5, height=5)
        self.button_login.grid(row=3, column=2)

        # Label Account Balance:
        self.account_label = ctk.CTkLabel(self.root, text="Account Balance:", font=("Arial", 15))
        self.account_label.pack(pady=(10, 0))

        # Label for balance amount
        self.balance_label = ctk.CTkLabel(self.root, text=f"${self.balance:.2f}", font=("Arial", 35, "bold"),
                                          text_color='green')
        self.balance_label.pack()

        # Go back button
        self.back_d_button = ctk.CTkButton(self.root, text="Back", font=("Arial", 15, "bold"), command=self.back_dw,
                                           width=250, height=50)
        self.back_d_button.pack(pady=(60, 30))

    def back_dw(self):
        # Clear deposit & withdraw screen
        self.dep_title_label.pack_forget()
        self.dep_frame.pack_forget()
        self.back_d_button.pack_forget()
        self.account_label.pack_forget()
        self.balance_label.pack_forget()

        # Create casino menu
        self.casino_menu()

    def dep_dw(self):
        try:
            # Amount entered in deposit entry field
            amount = float(self.dep_entry.get())
            # If valid amount
            if amount > 0:
                # Add amount to balance
                self.balance += amount
                # Update label
                self.update_balance_label()
            # If amount is negative or zero
            elif amount <= 0:
                messagebox.showerror("Casino Error", "Amount must be greater than zero")
            # If amount not number
            else:
                messagebox.showerror("Casino Error", "Invalid Character")
        except:
            messagebox.showerror("Casino Error", "Invalid Character")

    def with_dw(self):
        try:
            # Amount entered in withdraw field
            amount = float(self.with_entry.get())
            # If negative or zero amount
            if amount <= 0:
                messagebox.showerror("Casino Error", "Amount must be greater than zero")
            # Valid amount
            elif amount <= self.balance:
                # Subtract amount from balance
                self.balance -= amount
                # Update balance amount
                self.update_balance_label()
            # If Insufficient Account balance
            elif amount > self.balance:
                messagebox.showerror("Casino Error", "Insufficient Funds")
            # If not number
            else:
                messagebox.showerror("Casino Error", "Invalid Character")
        except:
            messagebox.showerror("Casino Error", "Invalid Character")

    def update_balance_label(self):
        # Update the balance label with balance amount
        self.balance_label.configure(text=f"${self.balance:.2f}")

    def view_history(self):
        # Clear menu
        self.clear_menu()

        # Title for view history page
        self.vh_title_label = ctk.CTkLabel(self.root, text="Your Game History", font=("Arial", 35, "bold"))
        self.vh_title_label.pack(pady=(30, 10))

        # Scrollable transaction history widget
        self.history_text = tk.scrolledtext.ScrolledText(self.root, height=20, width=60)
        self.history_text.pack()

        # Go back button
        self.back_vh_button = ctk.CTkButton(self.root, text="Back", font=("Arial", 15, "bold"), command=self.back_vh,
                                            width=250, height=50)
        self.back_vh_button.pack(pady=10)

    def back_vh(self):
        # Clear view history page
        self.back_vh_button.pack_forget()
        self.vh_title_label.pack_forget()
        self.history_text.pack_forget()

        # Create casino menu
        self.casino_menu()

    def logout(self):
        # Clear menu
        self.clear_menu()
        # Create login page
        self.create_login()

    def register(self):
        # Clear login page
        self.clear_login()

        # Register page title
        self.register_title_label = ctk.CTkLabel(self.root, text="Register an Account", font=("Arial", 35, "bold"))
        self.register_title_label.pack(pady=50)

        # Register frame
        self.register_frame = tk.Frame(self.root)
        self.register_frame.pack(pady=5)

        # User ID Entry
        self.login_label = ctk.CTkLabel(self.register_frame, text="User ID:", font=("Arial", 20))
        self.login_label.grid(row=0, column=0)
        self.login_entry = ctk.CTkEntry(self.register_frame, width=200)
        self.login_entry.grid(row=0, column=1)

        # Password Entry
        self.password_label = ctk.CTkLabel(self.register_frame, text="Password:", font=("Arial", 20))
        self.password_label.grid(row=1, column=0)
        self.password_entry = ctk.CTkEntry(self.register_frame, show="*", width=200)
        self.password_entry.grid(row=1, column=1)

        # Register button
        self.button_register = ctk.CTkButton(self.root, text="Register", command=self.register_button)
        self.button_register.pack(pady=15)

    def register_button(self):
        # Clear register page
        self.register_frame.pack_forget()
        self.register_title_label.pack_forget()
        self.button_register.pack_forget()

        # Create login page
        self.create_login()


def main():
    root = ctk.CTk()
    CasinoGui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
