bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}

def welcome():
    """
    Task: Show a welcome message.
    Name: welcome
    Input: None
    Side Effects: Print a welcome message.
    Return: None
    """
    print("Welcome to Berklee Bank!")

def login():
    """
    Task: Let the user log in to their bank account.
    Name: login
    Input: User's name and PIN.
    Side Effects: Ask the user to enter their name and PIN.
    Return: The user's account information if login is successful.
    """
    name = input("Enter your name: ")
    pin = input("Enter your PIN: ")

    if name in bank_dict:
        if bank_dict[name]["pin"] == pin:
            print("Login successful!")
            return bank_dict[name]
        else:
            print("Incorrect PIN.")
    else:
        print("Account not found.")

    return None

def show_menu():
    """
    Task: Show the ATM menu.
    Name: show_menu
    Input: None
    Side Effects: Display the four menu options.
    Return: None
    """
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance():
    """
    Task: Show the user's account balance.
    Name: check_balance
    Input: User's account information.
    Side Effects: Display the current balance.
    Return: None
    """
    name = input("Enter your name: ")

    if name in bank_dict:
        print("Your balance is:", bank_dict[name]["balance"])
    else:
        print("Account not found.")

def deposit():
    """
    Task: Let the user deposit money into their account.
    Name: deposit
    Input: The amount of money to deposit.
    Side Effects: Add money to the account balance.
    Return: None
    """
    name = input("Enter your name: ")

    if name in bank_dict:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            bank_dict[name]["balance"] += amount
            print("Deposit successful!")
            print("New balance:", bank_dict[name]["balance"])
        else:
            print("Invalid amount.")
    else:
        print("Account not found.")

def withdraw():
    """
    Task: Let the user withdraw money without exceeding their balance.
    Name: withdraw
    Input: The amount of money to withdraw.
    Side Effects: Take money out of the account balance.
    Return: None
    """
    name = input("Enter your name: ")

    if name in bank_dict:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")
        elif amount > bank_dict[name]["balance"]:
            print("Not enough money.")
        else:
            bank_dict[name]["balance"] -= amount
            print("Withdrawal successful!")
            print("New balance:", bank_dict[name]["balance"])
    else:
        print("Account not found.")

def exit_bank():
    """
    Task: Let the user exit the ATM program.
    Name: exit_bank
    Input: None
    Side Effects: Display a goodbye message.
    Return: None
    """
    print("Thank you for using Berklee Bank!")
    print("Goodbye!")

def run_unit_tests():
    print("Testing Berklee Bank functions")
    print("Test 1: Check account data")
    print("Test: Welcome")
    welcome()  # Expected: Welcome to Berklee Bank!

    print(bank_dict["Priya"]["balance"])  # Expected: 100
    print(bank_dict["Amira"]["balance"])  # Expected: 0
    print(bank_dict["Jordan"]["pin"])     # Expected: 9999

    
    
    print("Test 2: Check withdrawal amount")

    balance = 100
    amount = 50
    print(amount <= balance)  # Expected: True

    amount = 200
    print(amount <= balance)  # Expected: False

    
    
    print("Test 3: Check deposit")

    balance = 100
    amount = 50

    new_balance = balance + amount
    print(new_balance)  # Expected: 150


    
    print("Test 4: Check withdrawal")

    balance = 100
    amount = 50

    new_balance = balance - amount
    print(new_balance)  # Expected: 50



    print("Test 5: Check login")

    name = "Priya"
    pin = "4821"

    print(bank_dict[name]["pin"] == pin)  # Expected: True

    pin = "1234"
    print(bank_dict[name]["pin"] == pin)  # Expected: False

    
    
run_unit_tests()