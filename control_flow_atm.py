
print("Welcome to Jenvic ATM Machine")

Initial Setup
balance = 5000
pin = 1234
import getpass

User Authentication
attempts = 0
while attempts < 3:
    user_pin = getpass.getpass("Enter your PIN: ")
    if user_pin == str(pin):
        break
    attempts += 1
    print("Incorrect PIN. Try again.")
if attempts == 3:
    print("Too many incorrect attempts. Access blocked.")
    exit()

Main Menu
while True:
    print("\nMain Menu:")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Change PIN")
    print("5. Exit")
    choice = input("Enter your choice: ")

    # Check Balance
    if choice == "1":
        print(f"Current Balance: {balance}")

    # Deposit Funds
    elif choice == "2":
        while True:
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"New Balance: {balance}")
                    break
                else:
                    print("Invalid amount. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Withdraw Funds
    elif choice == "3":
        while True:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount > 0 and amount <= balance:
                    balance -= amount
                    print(f"New Balance: {balance}")
                    break
                elif amount > balance:
                    print("Insufficient balance.")
                else:
                    print("Invalid amount. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Change PIN
    elif choice == "4":
        while True:
            current_pin = getpass.getpass("Enter current PIN: ")
            if current_pin == str(pin):
                while True:
                    new_pin = getpass.getpass("Enter new PIN (4-digit): ")
                    if len(new_pin) == 4 and new_pin.isdigit():
                        confirm_pin = getpass.getpass("Confirm new PIN: ")
                        if confirm_pin == new_pin:
                            pin = int(new_pin)
                            print("PIN changed successfully.")
                            break
                        else:
                            print("PIN mismatch. Try again.")
                    else:
                        print("Invalid PIN. Please enter a 4-digit integer.")
                break
            else:
                print("Incorrect current PIN. Try again.")

    # Exit
    elif choice == "5":
        print("Thank you for using the ATM.")
        print(f"Total Deposits: {balance - 5000}")
        print(f"Total Withdrawals: {5000 - balance}")
        break

    else:
        print("Invalid choice. Please try again.")


