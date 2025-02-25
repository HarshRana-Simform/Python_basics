class BankAccount:
    '''
    This class represents the bank account and its associated function.
    '''

    def __init__(self,name :str,balance :float,account_number :int) -> None:
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

    def deposit(self, deposit_amount :float):
        '''
        Adds the amount to the current balance of the user

        Parameters:
            deposit_amount (float):Amount to be deposited
        '''

        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f"Amount deposited successfully! Your updated balance Rs.{self.balance}")

        else:
            print("Invalid amount added.")

    def withdraw(self, withdraw_amount :float):
        '''
        Subtracts the amount to the current balance of the user

        Parameters:
            withdraw_amount (float):Amount to be deposited
        '''

        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(f"Amount withdrawn successfully! Your updated balance Rs.{self.balance}")

        else:
            print(f"Insufficient funds! Balance: {self.balance}")

    def check_balance(self):
        '''
        Displays the current amount in the account.
        '''

        print(f"Your current balance is: Rs.{self.balance}")

    def transfer(self,other :object,transfer_amount :float):
        '''
        Transfer money from sender to receiver account.

        Parameters:
            other (object): The object of the receiver.
            transfer_amount (float): The amount to be transfered.
        '''
        if transfer_amount > 0:

            if self.balance > transfer_amount:

                self.balance -= transfer_amount
                other.balance += transfer_amount

                print(f"Transfer successful, your current balance is Rs.{self.balance}")

            else:

                print("Insufficient balance!!!")

        else:

            print("Invalid transfer amount. It must be positive.")


    def account_info(self):
        '''
        Displays the information about the selected account
        '''

        print(f"Account Name: {self.name}")
        print(f"Current Balance: Rs.{self.balance}")
        print(f"Account Number: {self.account_number}")

    def to_file(self):
        '''
        Converts the account object into simple string for storing in file
        '''
        return f'{self.account_number},{self.name},{self.balance}\n'


def to_obj(line :str):
    '''
    To convert the data read from file into bankaccount object

    Parameters:
    line (str): A single line from the accounts file

    Returns:
    BankAccount (object): An object of accounts info from the string line
    '''

    account_number, name, balance = line.strip().split(',')
    return BankAccount(name, float(balance), int(account_number))


# Function to save all the data in the file
def save_data(accounts,filename='accounts.txt'):
    '''
        Saves data into accounts.txt file
    '''

    with open(filename,'w') as file:
        for account in accounts.values():
            file.write(account.to_file())

# To load the data in the file to the dictionary so that it persists
def load_data():
    '''
        Loads data from the accounts.txt file into the accounts dictionary
    '''

    accounts = {}
    try:
        with open('accounts.txt','r') as file:
            for line in file:
                account = to_obj(line)
                accounts[account.account_number] = account

    except FileNotFoundError:
        print("No previous data found. You are the first customer.")

    return accounts


def main():

    accounts = load_data() #Dictionary to store accounts
    account_counter = len(accounts)+1 #A counter to generate account_numbers

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

        if choice == 1:

            name = input("Enter your name: ")
            balance = float(input("Enter the initial amount of deposit in your account: Rs."))
            account_number = account_counter
            account = BankAccount(name,balance,account_number)
            accounts[account_number] = account
            account_counter += 1
            save_data(accounts)
            print(f"Account created successfully, your account number is: {account_number}")

        elif choice == 2:

            account_number = int(input("Enter your account number: "))
            if account_number in accounts:
                deposit_amount = float(input("Enter the amount you want to deposit: Rs."))
                accounts[account_number].deposit(deposit_amount)
                save_data(accounts)
            else:
                print("Account does not exist!")

        elif choice == 3:

            account_number = int(input("Enter your account number: "))
            if account_number in accounts:
                deposit_amount = float(input("Enter the amount you want to withdraw: Rs."))
                accounts[account_number].withdraw(deposit_amount)
                save_data(accounts)
            else:
                print("Account does not exist!")

        elif choice == 4:

            account_number = int(input("Enter your account number: "))
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account does not exist!")

        elif choice == 5:

            sender_acc_number = int(input("Enter your account number: "))
            if sender_acc_number in accounts:

                receiver_acc_number = int(input("Enter the receiver's account number: "))

                if receiver_acc_number in accounts:

                    transfer_amount = float(input("Enter the amount of money to transfer: Rs."))
                    accounts[sender_acc_number].transfer(accounts[receiver_acc_number],
                    transfer_amount)
                    save_data(accounts)

                else:
                    print("The receiver's account does not exists.")

            else:

                print("Your account does not exists.")


        elif choice == 6:
            account_number = int(input("Enter your account number: "))
            if account_number in accounts:
                accounts[account_number].account_info()
            else:
                print("Account does not exist!")

        elif choice == 7:
            print("Thank you for banking with us!!!")
            break

        else:
            print("Enter a valid value.")


if __name__ == "__main__":
    main()
