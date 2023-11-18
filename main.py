import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class CasinoGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Casino")
        self.root.geometry("600x400")
        self.create_widgets()
        self.balance = 0

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="Welcome to the Casino!", font="Arial 35 bold")
        self.title_label.pack(pady=50)

        # Login and Password frame
        self.pass_log_frame = ttk.Frame(self.root)
        self.pass_log_frame.pack(pady=5)

        # Login Entry
        self.login_label = ttk.Label(self.pass_log_frame, text="Login ID:", font="Arial 15")
        self.login_label.grid(row=0, column=0)
        self.login_entry = ttk.Entry(self.pass_log_frame)
        self.login_entry.grid(row=0, column=1)

        # Password Entry
        self.password_label = ttk.Label(self.pass_log_frame, text="Password:", font="Arial 15")
        self.password_label.grid(row=1, column=0)
        self.password_entry = ttk.Entry(self.pass_log_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        # Login button
        self.button_login = tk.Button(self.root, text="Login", command=self.login)
        self.button_login.pack(pady=5)

        # Register button
        self.button_register = tk.Button(self.root, text="Register a new account", command=self.register)
        self.button_register.pack(pady=5)


    def clear_login(self):
        # Clear the login widgets
        self.title_label.pack_forget()
        self.pass_log_frame.pack_forget()
        self.button_login.pack_forget()
        self.button_register.pack_forget()
    def login(self):
        login_id = self.login_entry.get()
        password = self.password_entry.get()
        # Here you can add your login logic
        # If login is successful, you can proceed to the casino menu
        self.casino_menu()

    def casino_menu(self):
        # Clear login page
        self.clear_login()

        # Casino Menu Title
        self.menu_title_label = tk.Label(self.root, text="Casino Menu", font="Arial 35 bold")
        self.menu_title_label.pack(pady=35)

        # Play Button
        self.play_button = tk.Button(self.root, text="Play", font="Arial 15 bold", highlightbackground='red',
                                     command=self.play, width=30, height=2)
        self.play_button.pack(pady=5)

        # Deposit/Withdraw Button
        self.money_button = tk.Button(self.root, text="Deposit & Withdraw", font="Arial 15 bold",
                                      highlightbackground='green', command=self.deposit_withdraw, width=30, height=2)
        self.money_button.pack(pady=5)

        # View History Button
        self.history_button = tk.Button(self.root, text="View History", font="Arial 15 bold",
                                        highlightbackground='gold', command=self.view_history, width=30, height=2)
        self.history_button.pack(pady=5)

        # Logout Button
        self.logout_button = tk.Button(self.root, text="Logout", font="Arial 15 bold", highlightbackground='black',
                                       command=self.logout, width=30, height=2)
        self.logout_button.pack(pady=5)

    def clear_menu(self):
        # Clear casino menu
        self.menu_title_label.pack_forget()
        self.play_button.pack_forget()
        self.money_button.pack_forget()
        self.history_button.pack_forget()
        self.logout_button.pack_forget()
    def play(self):
        self.clear_menu()

        self.play_title_label = tk.Label(self.root, text="Choose a Game", font="Arial 35 bold")
        self.play_title_label.pack(pady=35)

        self.play_slots_button = tk.Button(self.root, text="Slots", font="Arial 15 bold",
                                           highlightbackground='red', width=30, height=2)
        self.play_slots_button.pack(pady=5)

        self.play_blackjack_button = tk.Button(self.root, text="Blackjack", font="Arial 15 bold",
                                               highlightbackground='black', width=30, height=2)
        self.play_blackjack_button.pack(pady=5)

        self.back_play_button = tk.Button(self.root, text="Back", font="Arial 15 bold", command=self.back_play,
                                          width=30, height=2)
        self.back_play_button.pack(pady=5)

    def back_play(self):
        self.back_play_button.pack_forget()
        self.play_title_label.pack_forget()
        self.play_slots_button.pack_forget()
        self.play_blackjack_button.pack_forget()
        self.casino_menu()

    def deposit_withdraw(self):
        self.clear_menu()

        self.dep_title_label = tk.Label(self.root, text="Deposit & Withdraw", font="Arial 35 bold")
        self.dep_title_label.pack(pady=35)

        self.dep_frame = ttk.Frame(self.root)
        self.dep_frame.pack(pady=5)

        # Login Entry
        self.login_label = ttk.Label(self.dep_frame, text="Amount:", font="Arial 15")
        self.login_label.grid(row=0, column=0)
        self.dep_entry = ttk.Entry(self.dep_frame)
        self.dep_entry.grid(row=0, column=1)

        self.button_login = tk.Button(self.dep_frame, text="Deposit", command=self.dep_dw, width=5)
        self.button_login.grid(row=0, column=2)

        self.login_label = ttk.Label(self.dep_frame, text="Amount:", font="Arial 15")
        self.login_label.grid(row=3, column=0)
        self.with_entry = ttk.Entry(self.dep_frame)
        self.with_entry.grid(row=3, column=1)

        self.button_login = tk.Button(self.dep_frame, text="Withdraw", command=self.with_dw, width=5)
        self.button_login.grid(row=3, column=2)

        self.account_label = tk.Label(self.root, text="Account Balance:", font="Arial 15")
        self.account_label.pack(pady=(10,0))

        self.balance_label = tk.Label(self.root, text=f"${self.balance:.2f}", font="Arial 15", fg='green')
        self.balance_label.pack()

        self.back_d_button = tk.Button(self.root, text="Back", font="Arial 15 bold", command=self.back__dw, width=30,
                                       height=2)
        self.back_d_button.pack(pady=(90, 5))

    def back__dw(self):
        self.dep_title_label.pack_forget()
        self.dep_frame.pack_forget()
        self.back_d_button.pack_forget()
        self.account_label.pack_forget()
        self.balance_label.pack_forget()
        self.casino_menu()

    def dep_dw(self):
        amount = float(self.dep_entry.get())
        if amount > 0:
            self.balance += amount
            self.update_balance_label()

    def with_dw(self):
        amount = float(self.with_entry.get())
        if amount <= self.balance:
            self.balance -= amount
            self.update_balance_label()

    def update_balance_label(self):
        self.balance_label.config(text=f"${self.balance:.2f}")

    def view_history(self):
        self.clear_menu()

        self.vh_title_label = tk.Label(self.root, text="Your Game History", font="Arial 35 bold")
        self.vh_title_label.pack(pady=(30,0))

        self.history_text = tk.scrolledtext.ScrolledText(self.root, highlightbackground='black', height=17, width=52)
        self.history_text.pack()

        self.back_vh_button = tk.Button(self.root, text="Back", font="Arial 15 bold", command=self.back_vh, width=30,
                                        height=2)
        self.back_vh_button.pack(pady=10)

    def back_vh(self):
        self.back_vh_button.pack_forget()
        self.vh_title_label.pack_forget()
        self.history_text.pack_forget()
        self.casino_menu()

    def logout(self):
        self.clear_menu()
        self.create_widgets()  # Re-create the login widgets

    def register(self):
        self.clear_login()
        self.register_title_label = tk.Label(self.root, text="Register an Account", font="Arial 35 bold")
        self.register_title_label.pack(pady=50)

        # Register frame
        self.register_frame = ttk.Frame(self.root)
        self.register_frame.pack(pady=5)

        # User ID Entry
        self.login_label = ttk.Label(self.register_frame, text="User ID:", font="Arial 15")
        self.login_label.grid(row=0, column=0)
        self.login_entry = ttk.Entry(self.register_frame)
        self.login_entry.grid(row=0, column=1)

        # Password Entry
        self.password_label = ttk.Label(self.register_frame, text="Password:", font="Arial 15")
        self.password_label.grid(row=1, column=0)
        self.password_entry = ttk.Entry(self.register_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        # Register button
        self.button_register = tk.Button(self.root, text="Register", command=self.register_button)
        self.button_register.pack(pady=5)

    def register_button(self):
        self.register_frame.pack_forget()
        self.register_title_label.pack_forget()
        self.button_register.pack_forget()
        self.create_widgets()

def main():
    root = tk.Tk()
    CasinoGui(root)
    root.mainloop()

if __name__ == "__main__":
    main()