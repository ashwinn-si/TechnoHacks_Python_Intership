#Celcius to Fahrenheit Convertor
def cel_fahrenheit():
    print("\nCelsius to Fahrenheit")
    temp=float(input("Enter the temperature in Celcius : "))
    result= (temp*(9/5))+32
    print("Celsius    : ",temp)
    print("Fahrenheit : ",result)

def fahrenheit_cel():
    print("\nFahrenheit to Celsius")
    temp=float(input("Enter the temperature in Celcius : "))
    result=(temp-32)*(5/9)
    print("Fahrenheit : ",temp)
    print("Celsius    : ",result)
print("TEMPERATURE CONVERTOR")
while(True):
    print("\nChoose (1/2)")
    print("1 . Celsius to Fahrenheit")
    print("2 . Fahrenheit to Celsius")
    x=int(input())
    if(x==1):
        cel_fahrenheit()
    elif(x==2):
        fahrenheit_cel()
    print("Do you want to continue(1/0)")
    de=int(input())
    if(de==0):
        print("*******THANK YOU**********")
        break
