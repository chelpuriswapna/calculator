#caluculator 
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return"error!division by zero"
    return x/y
while True:
    print("select  a operation")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.divide")

#take an input from user
    choice=input("enter choice(1/2/3/4):")
#check if one of in  four options
    if choice in('1','2','3','4'):
        try:
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))

        except ValueError:
            print("invalid input. please enter a number")
            continue
        if choice=='1':
            print(num1,"+",num2,"=",addition(num1,num2))
        if choice=='2':
            print(num1,"-",num2,"=",subtraction(num1,num2))
        if choice=='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        if choice=='4':
            print(num1,"/",num2,"=",divide(num1,num2))
#check if user want another calculator
    #break the while loop if user answer is no
        next_calculator=input("let's do next calculation?(yes/no):")
        if next_calculator.lower()=="no":
            print("existing calculator.goodbye")
            break
        else:
            print("invalid input.please select valid operation")
        

                   
