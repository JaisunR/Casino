import datetime # pip install datetime
import tkinter as tk  # pip install tkinter
import customtkinter as ctk  # pip install customtkinter
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import slotmachine
import blackjack
import database
import client
import server

class CasinoGui:
    def __init__(self, root):
        # Create initial window
        self.root = root
        self.root.title("Casino")
        self.root.geometry("600x400")
        self.create_login()
        self.balance = 0

    # Login Page
    def create_login(self): # Create login page
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
        self.user_id = self.login_entry.get()
        self.password = self.password_entry.get()

        # Check if username and password are both entered
        if not self.user_id or not self.password:
            messagebox.showerror("Casino Error", "Please enter both username and password")
            return
        user = database.user.find_one(
            {"username": self.user_id, "password": self.password}
        )
        if not user:
            messagebox.showerror(
                "Casino Error", "Please provide valid user_id and password"
            )
        else:
            self.casino_menu()

    # Register Page
    def register(self): # Creates the register page
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
        self.button_register.pack(pady=(15, 5))

        # Go back button
        self.back_login_button = ctk.CTkButton(self.root, text="Back", command=self.back_login)
        self.back_login_button.pack()

    def back_login(self):  # Clears the screen, brings user back to the login menu
        # Clear deposit & withdraw screen
        self.register_title_label.pack_forget()
        self.register_frame.pack_forget()
        self.login_label.pack_forget()
        self.login_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.button_register.pack_forget()
        self.back_login_button.pack_forget()

        # Create login menu
        self.create_login()

    def register_button(self): # Registers a user account if not credentials don't already exist
        self.user_id = self.login_entry.get()
        self.password = self.password_entry.get()

        # Check if username and password are entered
        if not self.user_id or not self.password:
            messagebox.showerror("Casino Error", "Please enter both a username and password")
            return
        # Check if username exists in database
        if database.user.find_one({"username": self.user_id}):
            # Return Error
            messagebox.showerror("Casino Error", "User name already exists")
        else:
            self.set_user(self.user_id, self.password)
            # Clear register page
            self.register_frame.pack_forget()
            self.register_title_label.pack_forget()
            self.button_register.pack_forget()
            self.back_login_button.pack_forget()

            # Create login page
            self.create_login()

    def set_user(self, user_id, password):
        # setting up user account
        user_data = {"username": user_id, "password": password}
        database.user.insert_one(user_data)

        # setting up balance account
        balance_data = {"username": user_id, "balance": 0}
        database.balance.insert_one(balance_data)

    def casino_menu(self): # Creates the casino main menu
        self.balance = database.balance.find_one({"username": self.user_id})["balance"]
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

        self.chat_button = ctk.CTkButton(self.root, text="Chat", font=("Arial", 15, "bold"),
                                            command=self.chat, width=250, height=50)
        self.chat_button.pack(pady=5)

        # Logout Button
        self.logout_button = ctk.CTkButton(self.root, text="Logout", font=("Arial", 15, "bold"),
                                           command=self.logout, width=250, height=50)
        self.logout_button.pack()

    def clear_menu(self):
        # Clear casino menu
        self.menu_title_label.pack_forget()
        self.play_button.pack_forget()
        self.money_button.pack_forget()
        self.history_button.pack_forget()
        self.logout_button.pack_forget()
        self.chat_button.pack_forget()

    # Play Page
    def play(self):  # Creates the play page with the 2 available games
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

    # Slots Game Page
    def slots_play(self):  # Creates the page for the slots game
        # Clear play screen
        self.back_play_button.pack_forget()
        self.play_title_label.pack_forget()
        self.play_slots_button.pack_forget()
        self.play_blackjack_button.pack_forget()

        # If Windows use 175,175
        # If Mac use 125,125
        # Size of Images
        new_size = (175, 175)

        # Load and resize slot machine images into variables
        self.img7 = ImageTk.PhotoImage(Image.open("Slots Symbols/7.png").resize(new_size))
        self.imgCherry = ImageTk.PhotoImage(Image.open("Slots Symbols/Cherry.png").resize(new_size))
        self.imgBell = ImageTk.PhotoImage(Image.open("Slots Symbols/Bell.png").resize(new_size))
        self.imgWatermelon = ImageTk.PhotoImage(Image.open("Slots Symbols/Watermelon.png").resize(new_size))
        self.imgBanana = ImageTk.PhotoImage(Image.open("Slots Symbols/Banana.png").resize(new_size))

        # Slots title
        self.title_label = ctk.CTkLabel(self.root, text="Slots!", font=("Arial", 30, "bold", "italic"))
        self.title_label.pack(pady=25)

        self.subtext_label = ctk.CTkLabel(self.root, text="Match All 3 To 10x Your Money!", font=("Arial", 12, "bold", "italic"))
        self.subtext_label.pack()

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
                database.balance.update_one(
                    {"username": self.user_id}, {"$inc": {"balance": -amount}}
                )
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
                    database.balance.update_one(
                        {"username": self.user_id}, {"$inc": {"balance": amount * 10}}
                    )
                    self.balance += amount * 10
                    self.update_balance_label()
                    # Update game history as win
                    user_balance = self.balance
                    self.log_game_history("Slots", "WIN!", amount, user_balance)
                else:
                    # Update game history as loss
                    user_balance = self.balance
                    self.log_game_history("Slots", "LOSS", amount, user_balance)
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
        self.subtext_label.pack_forget()

        # Creates play screen
        self.play()

    # Blackjack game page
    def blackjack_play(self): # Creates the blackjack page
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
        self.hit_button = ctk.CTkButton(self.hs_frame, text="Hit", font=("Arial", 15, "bold"),
                                        command=self.hit, width=60, height=30, state=tk.DISABLED)
        self.hit_button.grid(row=0, column=1, padx=(0, 5))

        # Stand button
        self.stand_button = ctk.CTkButton(self.hs_frame, text="Stand", font=("Arial", 15, "bold"),
                                        command=self.stand, width=60, height=30, state=tk.DISABLED)
        self.stand_button.grid(row=0, column=2)

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
        self.bet_placed = False
        try:
            # Get amount from entry field
            self.bj_amount = float(self.bet_entry.get())
            # Error handling for negatives and zero amounts
            if self.bj_amount <= 0:
                messagebox.showerror("Casino Error", "Amount must be greater than zero")
            # Correct Entry
            elif self.bj_amount <= self.balance:
                self.bet_placed = True
                # Subtract amount from balance and update balance label
                database.balance.update_one({"username": self.user_id}, {"$inc": {"balance": -self.bj_amount}})
                self.balance -= self.bj_amount
                self.update_balance_label()

                self.reset_blackjack()

                # Enable Hit and Stand buttons
                self.hit_button.configure(state=tk.NORMAL)
                self.stand_button.configure(state=tk.NORMAL)

                self.player_value = blackjack.calculate_hand_value(self.player_hand)

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
                self.dealer_value = blackjack.calculate_hand_value(self.dealer_hand)

                while self.dealer_value <= 16:
                    blackjack.deal_card(self.dealer_hand, self.deck)
                    self.dealer_value = blackjack.calculate_hand_value(self.dealer_hand)

                print(self.player_hand)
                print(self.dealer_hand)

            # Error handling for Insufficient Balance
            elif self.bj_amount > self.balance:
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

    def hit(self):
        try:
            blackjack.deal_card(self.player_hand, self.deck)
            if len(self.player_hand) == 3:
                self.uCard3.configure(image=self.card_images[self.player_hand[2]])
            elif len(self.player_hand) == 4:
                self.uCard4.configure(image=self.card_images[self.player_hand[3]])
            self.your_value = blackjack.calculate_hand_value(self.player_hand)
            self.your.configure(text=f"Your: {self.your_value}")
            if self.your_value > 21:
                messagebox.showinfo("Blackjack", "You Lose")
                # Disable Hit and Stand buttons
                self.hit_button.configure(state=tk.DISABLED)
                self.stand_button.configure(state=tk.DISABLED)
                # Log game entry
                self.log_game_history("Blackjack", "LOSS", self.bj_amount, self.balance)
                self.reset_blackjack()
        except:
            messagebox.showerror("Casino Error", "Place Bets First")

    def stand(self):
        try:
            self.dealer.configure(text=f"Dealer: {self.dealer_value}")
            self.dCard2.configure(image=self.card_images[self.dealer_hand[1]])
            if len(self.dealer_hand) > 2:
                self.dCard3.configure(image=self.card_images[self.dealer_hand[2]])
            if len(self.dealer_hand) > 3:
                self.dCard4.configure(image=self.card_images[self.dealer_hand[3]])
            result = blackjack.check_win(self.dealer_value, self.your_value)
            if result == 1:
                messagebox.showinfo("Blackjack", "You Win!")
                # Disable Hit and Stand buttons
                self.hit_button.configure(state=tk.DISABLED)
                self.stand_button.configure(state=tk.DISABLED)
                database.balance.update_one({"username": self.user_id}, {"$inc": {"balance": self.bj_amount * 2}})
                self.log_game_history("Blackjack", "WIN!", self.bj_amount, self.balance)
                self.balance += self.bj_amount * 2
                self.balance_label.configure(text=f"${self.balance:.2f}")
            elif result == -1:
                messagebox.showinfo("Blackjack", "You lose")
                # Disable Hit and Stand buttons
                self.hit_button.configure(state=tk.DISABLED)
                self.stand_button.configure(state=tk.DISABLED)
                self.log_game_history("Blackjack", "LOSS", self.bj_amount, self.balance)
            elif result == 0:
                messagebox.showinfo("Blackjack", "Draw")
                # Disable Hit and Stand buttons
                self.hit_button.configure(state=tk.DISABLED)
                self.stand_button.configure(state=tk.DISABLED)
                # Add money back into account
                database.balance.update_one({"username": self.user_id}, {"$inc": {"balance": self.bj_amount}})
                self.balance += self.bj_amount
                self.balance_label.configure(text=f"${self.balance:.2f}")
                # Log game history
                self.log_game_history("Blackjack", "DRAW", self.bj_amount, self.balance)
            self.reset_blackjack()
        except:
            messagebox.showerror("Casino Error", "Place Bets First")

    def reset_blackjack(self):

        # Clear user and dealer hand
        self.player_hand = []
        self.dealer_hand = []

        # Reset user and dealer hand value
        self.your_value = 0
        self.dealer_value = 0

        # Create new deck
        self.deck = blackjack.create_deck()

        # Reset all cards to "face down"
        self.uCard1.configure(image=self.card_default)
        self.uCard2.configure(image=self.card_default)
        self.uCard3.configure(image=self.card_default)
        self.uCard4.configure(image=self.card_default)

        self.dCard1.configure(image=self.card_default)
        self.dCard2.configure(image=self.card_default)
        self.dCard3.configure(image=self.card_default)
        self.dCard4.configure(image=self.card_default)

        self.your.configure(text=f"Your Hand: {self.your_value}")
        self.dealer.configure(text=f"Dealer's Hand: {self.dealer_value}")

    def blackjack_back(self):
        # Clear blackjack screen
        self.title_label.pack_forget()
        self.back_button.pack_forget()
        self.bet_frame.pack_forget()
        self.hs_frame.pack_forget()
        self.card_frame.pack_forget()
        self.value_frame.pack_forget()

        # Create play menu
        self.play()

    def back_play(self):
        # Clear play screen
        self.back_play_button.pack_forget()
        self.play_title_label.pack_forget()
        self.play_slots_button.pack_forget()
        self.play_blackjack_button.pack_forget()

        # Create casino menu
        self.casino_menu()

    # Deposit/Withdraw Page
    def deposit_withdraw(self): # Creates the deposit/withdraw page
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

    def dep_dw(self): # Function for adding "money" into user account
        try:
            # Amount entered in deposit entry field
            amount = float(self.dep_entry.get())
            # If valid amount
            if amount > 0:
                # Add amount to balance
                self.balance = database.balance.find_one({"username": self.user_id})[
                    "balance"
                ]
                database.balance.update_one(
                    {"username": self.user_id}, {"$inc": {"balance": amount}}
                )
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

    def with_dw(self): # Function for withdrawing from user account
        try:
            # Amount entered in withdraw field
            amount = float(self.with_entry.get())
            # If negative or zero amount
            self.balance = database.balance.find_one({"username": self.user_id})[
                "balance"
            ]
            if amount <= 0:
                messagebox.showerror("Casino Error", "Amount must be greater than zero")
            # Valid amount
            elif amount <= self.balance:
                # Subtract amount from balance
                database.balance.update_one(
                    {"username": self.user_id}, {"$inc": {"balance": -amount}}
                )
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


    #View History Page
    def view_history(self):  # Creates the view history page
        # Clear menu
        self.clear_menu()

        # Title for view history page
        self.vh_title_label = ctk.CTkLabel(self.root, text="Your Game History", font=("Arial", 35, "bold"))
        self.vh_title_label.pack(pady=(30, 10))

        # Scrollable transaction history widget
        self.history_text = tk.scrolledtext.ScrolledText(self.root, height=25, width=100, font=("Arial", 20, "bold"))
        self.history_text.pack()

        # Display user history
        history_entries = database.game_history.find({"username": self.user_id})
        for entry in history_entries:
            self.history_text.insert(tk.END,
                                     f"{entry['timestamp']}   -   {entry['game_type']}   -   Result: {entry['result']} - "
                                     f"  Bet Amount: ${entry['bet_amount']}   -   Updated Balance: ${entry['updated_balance']}\n\n")
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

    def chat(self):
        self.clear_menu()
        client.client()

        self.vh_title_label = ctk.CTkLabel(self.root, text="Live Chat", font=("Arial", 35, "bold"))
        self.vh_title_label.pack(pady=(30, 10))

        self.chat_text = tk.scrolledtext.ScrolledText(self.root, height=15, width=100, font=("Arial", 20, "bold"))
        self.chat_text.pack()

        # Frame to contain the text entry and "Send" button
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.text_entry = tk.Entry(self.entry_frame, font=("Arial", 35), width=50)
        self.text_entry.pack(side=tk.LEFT, padx=(0,10))

        self.send_button = ctk.CTkButton(self.entry_frame, text="Send", font=("Arial", 15, "bold"),
                                         # command=self.send_message,
                                         width=15, height=3)
        self.send_button.pack(side=tk.LEFT)

        self.back_c_button = ctk.CTkButton(self.root, text="Back", font=("Arial", 15, "bold"), command=self.chat_back,
                                           width=250, height=50)
        self.back_c_button.pack(pady=10)

    def chat_back(self):
        self.vh_title_label.pack_forget()
        self.chat_text.pack_forget()
        self.back_c_button.pack_forget()
        self.text_entry.pack_forget()
        self.send_button.pack_forget()
        self.entry_frame.pack_forget()


        self.casino_menu()

    def logout(self):
        # Clear menu
        self.clear_menu()
        # Create login page
        self.create_login()

    def log_game_history(self, game_type, result, bet_amount, updated_balance):  # Function for logging each game entry
        timestamp = datetime.datetime.now()
        history_entry = {
            "username": self.user_id,
            "game_type": game_type,
            "result": result,
            "bet_amount": bet_amount,
            "timestamp": timestamp,
            "updated_balance": updated_balance
        }
        database.game_history.insert_one(history_entry)


# Main function
def main():
    root = ctk.CTk()
    CasinoGui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
