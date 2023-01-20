from abc import ABC, abstractmethod
class AccountInterface:
    @abstractmethod
    def display(self):
        pass
        
    @abstractmethod
    def addAccount(self, account):
        pass 
    
class BankAccount(AccountInterface):
    def __init__(self):
        self.__accounts = ['peter', 'tom', 'jim', 'lily']
        
    def display(self):
        nums = len(self.__accounts)
        print(f"There are {nums} accounts: {' '.join(self.__accounts)}")
        
    def addAccount(self, account):
        self.__accounts.append(account)
        print(f'Added account {account}')
        
class AccountProxy(AccountInterface):
    # protection proxy to BankAccount
    def __init__(self):
        self.bankAccount = BankAccount()
        self.secret = 'npuloveyou'
        
    def display(self):
        self.bankAccount.display()
        
    def addAccount(self, account):
        sec = input('What is the secret? ')
        self.bankAccount.addAccount(account) if sec == self.secret else print("That's incorrect!")
        
def main():
    accountProxy = AccountProxy()
    while True:
        print('1. Display list,  2. Add account,  3. quit')
        option = input('Select option: ')
        if option == '1':
            accountProxy.display()
        elif option == '2':
            name = input('Enter account name: ')
            accountProxy.addAccount(name)
        elif option == '3':
            exit() 
        else:
            print(f'unknown option: {option}')
            
if __name__ == '__main__':
    main()