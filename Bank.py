from User import User
class Bank:
    def __init__(self):
        self.Bank_amount = 10000
        self.Current_loan_Amount = 0
        self.loan_features = True
        self.User = []
        self.Admin = []
    
    def Create_Bank_Account_As_a_User(self,email,amount):
        self.email = email
        self.amount = amount
        self.User.append(email)
        return User(email,amount)
    
    def Create_Bank_Account_As_a_Admin(self,email):
        self.email = email
        self.Admin.append(email)
    
    def bank_available_balance(self):
        return self.Bank_amount

    def Total_loan_Amount(self):
        return self.Current_loan_Amount
    
    def loan_feature(self):
        return self.loan_features
    
    def Turn_on_loan_feature(self):
        self.loan_features = True
        print("Successfully You set,Loan feature is  available")
    
    def Turn_of_laon_feature(self):
        if self.loan_features == True:
            self.loan_features = False
            print("Successfully You set, loan feature are not available")
   
    def Aproved_for_loan(self,amount):
        self.Current_loan_Amount += amount*2
        self.Bank_amount -= amount
    
    