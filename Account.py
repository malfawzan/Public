class account:
    
    """account class is to create  objects for an account with some basic methods deposit , withdraw , getbalance and getname"""
   
    def __init__ (self, name):
        
        """Constructor to initialise the objects of account class"""
        
        self.__account_name=name   #private data variables initialising using double underscore __
        self.__account_balance=0