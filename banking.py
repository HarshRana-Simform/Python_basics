class BankAccount:
    '''
    This class represents the bank account and its associated function.
    '''

    def __init__(self,name :str,balance :float,account_number :int):
        '''
        Constructor to initialize the name, balance and account number on creating a account.

        Parameters:
            name (str):Name of the account holder.
            balance (float):Money present in the account. 
            account_number (int):Unique integer for every account
        '''
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def deposit(self,deposit_amount :float):
        '''
        Adds the amount to the current balance of the user

        Parameters:
            deposit_amount (float):Amount to be deposited 
        '''
        if deposit_amount > 0: 
            self.balance += deposit_amount
            print(f"Amount deposited successfully! Your updated balance {self.balance}")

        else: 
            print("Invalid amount added.")

    def withdraw(self,withdraw_amount :float):
        '''
        Subtracts the amount to the current balance of the user

        Parameters:
            withdraw_amount (float):Amount to be deposited 
        '''
        if withdraw_amount<self.balance:
            self.balance -= withdraw_amount
            print(f"Amount withdrawn successfully! Your updated balance {self.balance}")

        else:
            print(f"Insufficient funds! Balance: {self.balance}")

    def check_balance(self):
        '''
        Displays the current amount in the account. 
        '''
        print(f"Your current balance is: {self.balance}")

    def account_info(self):
        '''
        Displays the information about the selected account 
        '''
        print(f"Account Name: {self.name}")
        print(f"Current Balance: {self.balance}")
        print(f"Account Number: {self.account_number}")





    
def main():

    accounts = {} #Dictionary to store accounts 
    account_counter = 1 #A counter to generate account_numbers

    while True:

        print("-----Welcome to the HR Bank-----")
        print("1. Create an Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. View Account Information")
        print("7. Exit")
        
        choice = int(input("Select the service you want to use: "))

        if (choice == 1):
            
            name = input("Enter your name: ")
            balance = float(input("Enter the initial amount of deposit in your account: Rs."))
            account_number = account_counter
            account = BankAccount(name,balance,account_number)
            accounts[account_number] = account
            account_counter += 1
            print(f"Account created successfully, your account number is: {account_number}")

        elif (choice == 2):

            account_number = int(input("Enter your account number: "))
            if(account_number in accounts):
                deposit_amount = float(input("Enter the amount you want to deposit: Rs."))
                accounts[account_number].deposit(deposit_amount)
            else:
                print("Account does not exist!")

        elif (choice == 3):
            
            account_number = int(input("Enter your account number: "))
            if(account_number in accounts):
                deposit_amount = float(input("Enter the amount you want to withdraw: Rs."))
                accounts[account_number].withdraw(deposit_amount)
            else:
                print("Account does not exist!")

        elif (choice == 4):
            
            account_number = int(input("Enter your account number: "))
            if(account_number in accounts):
                accounts[account_number].check_balance()
            else:
                print("Account does not exist!")

        elif (choice == 5):
            pass

        elif (choice == 6):
            account_number = int(input("Enter your account number: "))
            if(account_number in accounts):
                accounts[account_number].account_info()
            else:
                print("Account does not exist!")

        elif (choice == 7):
            print("Thank you for banking with us!!!")
            break

        else:
              print("Enter a valid value.")



if __name__ == "__main__":
    main()