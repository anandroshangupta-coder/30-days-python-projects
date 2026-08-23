# ==========================================
# Day 16 - Bank Account Simulator
# 30 Days Python GitHub Project Challenge
# ==========================================

print("======================================")
print("        BANK ACCOUNT SIMULATOR")
print("======================================")


# Bank Account Class
class BankAccount:

    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    # Deposit money
    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f"\n✅ ₹{amount:.2f} deposited successfully.")
        else:
            print("\n❌ Deposit amount must be greater than 0.")

    # Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            print("\n❌ Withdrawal amount must be greater than 0.")

        elif amount > self.balance:
            print("\n❌ Insufficient balance.")

        else:
            self.balance -= amount
            print(f"\n✅ ₹{amount:.2f} withdrawn successfully.")

    # Check balance
    def check_balance(self):

        print("\n======================================")
        print("           ACCOUNT BALANCE")
        print("======================================")
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : ₹{self.balance:.2f}")
        print("======================================")

    # Display account information
    def account_details(self):

        print("\n======================================")
        print("         ACCOUNT INFORMATION")
        print("======================================")
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : ₹{self.balance:.2f}")
        print("======================================")


# Create account
print("\nCreate Your Bank Account")

account_holder = input("Enter account holder name: ")
account_number = input("Enter account number: ")

try:
    initial_deposit = float(input("Enter initial deposit: ₹"))

    if initial_deposit < 0:
        print("❌ Initial deposit cannot be negative.")
        initial_deposit = 0

except ValueError:
    print("❌ Invalid amount. Starting balance set to ₹0.")
    initial_deposit = 0


# Create BankAccount object
account = BankAccount(
    account_holder,
    account_number,
    initial_deposit
)


print("\n✅ Bank account created successfully!")


# Main menu
while True:

    print("\n======================================")
    print("              BANK MENU")
    print("======================================")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")
    print("======================================")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":

        try:
            amount = float(input("\nEnter deposit amount: ₹"))
            account.deposit(amount)

        except ValueError:
            print("\n❌ Please enter a valid amount.")

    elif choice == "2":

        try:
            amount = float(input("\nEnter withdrawal amount: ₹"))
            account.withdraw(amount)

        except ValueError:
            print("\n❌ Please enter a valid amount.")

    elif choice == "3":

        account.check_balance()

    elif choice == "4":

        account.account_details()

    elif choice == "5":

        print("\n======================================")
        print("   Thank You for Using Our Bank! 👋")
        print("======================================")
        break

    else:

        print("\n❌ Invalid choice! Please select 1-5.")