from User import User
from Bank import Bank

def main():
    open_bank = Bank()

    print("______________ User History ______________")
    Tom = open_bank.Create_Bank_Account_As_a_User("Tom@gmail.com",1000)
    jon = open_bank.Create_Bank_Account_As_a_User("jon@gmail.com",300)

    Tom.Deposite(1000)
    Tom.Withdraw(200)
    Tom.Deposite(500)
    Tom.Transfer_Another_User(jon,1000)
    Tom.Loan_request(open_bank)
    Tom.Check_balance()
    user1 = Tom.Transaction()
   
    for i in user1:
        print(i)
    print("\n")
    jon.Deposite(1000)
    jon.Withdraw(200)
    jon.Deposite(100)
    jon.Transfer_Another_User(jon,1200)
    jon.Check_balance()
    user2 = jon.Transaction()
    
    for i in user2:
        print(i)

    print("__________________________________________")
    

    print("______________ Admin Zone ______________")
    admin = Bank()
    admin.Create_Bank_Account_As_a_Admin("Admin@gmail.com")
    balance = admin.bank_available_balance()
    print("Bank Total Amount is :",balance)
    loan = admin.Total_loan_Amount()
    print(f'Bank Current Total loan pending :{loan}')
    admin.Turn_on_loan_feature()
    admin.Turn_of_laon_feature()
    Tom.Loan_request(open_bank)




if __name__ == '__main__':
    main()