def deposit(self, amount):
        
        """deposit(amount) method deposits or add specified amount to the account balance"""
        #deposit method
        
        if amount>0:  #amount checking
            
            self.__account_balance=self.__account_balance+amount # updating the balance here
            
            return True
        
        else:
            
            return False
            
    def withdraw(self, amount):

        """withdraw(amount) method to withdraw the specified amount from the account balance"""
        #withdraw method
        
        if amount>0: #amount checking
            
            if amount<=self.__account_balance:  #limit checking
                
                self.__account_balance=self.__account_balance-amount  #updating bank balance- amount reduction
                
                return True
            
            else:
                
                return False
        else:
            
            return False
        
    def getbalance(self):
        
        """getter method to get the private variable __account_balance alias bank balance amount"""
        
        return self.__account_balance  #returning balance
        
    def getname(self):

        """getter method to get the private variable __account_name alias bank holder name"""
        
        return self.__account_name   #returning name