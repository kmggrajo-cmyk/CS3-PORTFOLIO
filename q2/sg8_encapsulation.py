class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = 0
        self.set_balance(balance)
        
    def set_account_number(self,account_number):
        self.__account_number = account_number
        # sets the account number
  
    def get_account_number(self):
        return self.__account_number
      # allows access to private account number
  
    def set_balance(self, balance):
        if balance < 0:
            print("The balance must not be a negative number.")
        else: 
          self.__balance = balance 
        # if the value givne is negative, 
    
    def get_balance(self):
        return self.__balance
      # allows user to access balance


object = BankAccount(12345, 1000.0)
print("Account 1")
print(f"Account Number: {object.get_account_number()}")
print(f"Balance: {object.get_balance():.2f}") #.2f displayes two decimal places

print("\nUpdate balance  to -100")
object.set_balance(-100) #update balance

print(f"Account Number:{object.get_account_number()}") #print new data
print(f"Balance: {object.get_balance():.2f}")
            
            
    
        
        
        
        
    
        