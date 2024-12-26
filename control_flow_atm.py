## initial setup 
print(Welcome to jenvic ATM_Machine)

--ATM Machine Simulation

Initial Setup
balance = 5000

import getpass 
pin = 1234

User Authentication
attempts = 0
while attempts < 3:
    user_pin = int(input("Enter your PIN: "))
    if user_pin == pin:
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
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"New Balance: {balance}")

    # Withdraw Funds
    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"New Balance: {balance}")
        else:
            print("Insufficient balance.")

    # Change PIN
    elif choice == "4":
        current_pin = int(input("Enter current PIN: "))
        if current_pin == pin:
            new_pin = int(input("Enter new PIN (4-digit): "))
            if len(str(new_pin)) == 4:
                pin = new_pin
                print("PIN changed successfully.")
            else:
                print("Invalid PIN. Please try again.")

    # Exit
    elif choice == "5":
        print("Thank you for using the ATM.")
        print(f"Total Deposits: {balance - 5000}")
        print(f"Total Withdrawals: {5000 - balance}")
        break

    else:
        print("Invalid choice. Please try again.")

