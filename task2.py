import random
def rock_paper_scissor():
    while(True):
        computer_choice=random.choice([1,2,3])
        print("\nenter your choice(1/2/3) : ")
        your_choice=int(input())
        if(computer_choice==your_choice):
            print("******* WIN *********")
        else:
            print("******* LOSS *********")
        print("Do you want to continue(1/0)")
        de=int(input())
        if(de==0):
            print("*******THANK YOU**********")
            return
    

print("ROCK - PAPER - SCISSOR ")
print('''1 - Rock
2 - Paper
3 - Scissor''')
rock_paper_scissor() 