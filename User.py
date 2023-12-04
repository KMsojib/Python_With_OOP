class User:
    def __init__(self,email,user_balance):
        self.email = email
        self.user_balance = user_balance
        self.Transaction_history = []
    
    def Deposite(self,amount):
        self.user_balance += amount
        s = f"Deposite Amount : ${amount}"
        self.Transaction_history.append(s)
    
    def Withdraw(self,amount):
        if self.user_balance >= amount:    
            self.user_balance -= amount
            s = f"Withdraw Amount: ${amount}"
            self.Transaction_history.append(s)
        else:
            print("Unable to witdraw")
    

    def Transfer_Another_User(self,recipent,amount):
        if self.user_balance >= amount:
            self.user_balance -= amount
            recipent.Deposite(amount)
            s = f"Transfer Amount ${amount} and receiver is {recipent.email}"
            self.Transaction_history.append(s)
        else:
            print("Sorry! Your account is not sufficient")
    
    def Check_balance(self):
        print("Your Account Balance is : ",self.user_balance,"$")
    
    def Transaction(self):
        return self.Transaction_history
    
    def Loan_request(self,Bank):
        amount = self.user_balance*2
        if Bank.loan_feature() and amount <= Bank.bank_available_balance():
            self.Deposite(amount)
            Bank.Aproved_for_loan(amount)
            s = f"Loan Amount :{amount} is Aproved by Admin"
            self.Transaction_history.append(s)
            # print(s)
        else:
            print("Denied,Bank has Insufficient Fund")