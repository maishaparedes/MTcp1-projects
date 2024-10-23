# Maisha Tapia profiency

class BankAccount:
#Defines account number, totals the balance
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
#Adds the self balance to the amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
#Subracts self balance to the amount
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
#Returns self balance 
    def get_balance(self):
        return self.balance
#Asks user for initial balance and account number to return it
def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)
 #Creates total of each account and prints balance 
def main():
    accounts = {}
    #This while conditional prints the deposit withdrawl and allows the user to view their account and leave
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
     #This conditional creates account for user   
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
     #Runs many conditionals 
     #Each conditional checks for your account and asks the user they want to deposit an amount, if the user does not have enough it will make it invalid
        elif choice in ['2', '3', '4']:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")
        
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
#This conditional checks if the name is equal to the main and if it is it runs the main function 
if __name__ == "__main__":
    main()