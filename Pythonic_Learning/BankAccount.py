class BankAccount:
    _money=0

    def deposit(self, amount, password):
        if password == 'secret':
            self._money += amount
            print(f'You have deposited {amount}. Your balance is now {self._money}')
        else:
            return 'wrong password'

    def withdraw(self, amount, password):
        if password == 'secret':
            self._money -= amount
            print(f'You have withdrawn {amount}. Your balance is now {self._money}')
        else:
            return print('wrong password, try again!')
        
    def get_balance(self, password):
        if password == 'secret':
            return print(f'Your balance is {self._money}')
        else:
            return print('wrong password, try again!')
    
if __name__ == '__main__':
    ba = BankAccount()
    ba.deposit(100, 'secret')
    ba.get_balance('secret')
    ba.withdraw(50, 'secret')
    ba.get_balance('secret')
    ba.get_balance('wrong password')
    
