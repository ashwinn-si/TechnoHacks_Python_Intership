import random
def atm_stimulator():
    balance_amount=random.randint(0,10000)
    while(True):
        user_input=int(input("\nEnter your Choice(1/2/3/4) : "))
        if(user_input==1):
            print("\nCHECKING BALANCE....")
            print("Balance :",balance_amount)
        elif(user_input==3):
            print("\nTO WITHDRAW")
            with_draw_amount=int(input("Enter the amount to withdraw : "))
            if(with_draw_amount>balance_amount):
                print("Insufficient Balance")
                continue
            print("Check the cash box")
        elif(user_input==2):
            print("\nTO DEPOSIT")
            deposit_amount=int(input("Amount to deposit : "))
            balance_amount+=deposit_amount
            print("Amount successfully Deposited")
        elif(user_input==4):
            print("*******THANK YOU**********")
            return()
        else:
            print("\n***WRONG OPERATION***")

print("WELCOME TO TECHNOHACK ATM ")
print('''1 - Check Balance
2 - Deposit
3 - Withdraw
4 - EXIT''')
atm_stimulator()

