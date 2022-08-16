def calc():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    print("Select the operator you want to perform:")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 modulus")
    operation=input("Please choose an operation from these(1,2,3,4,5):")
    flag=True
    if operation=="1":
        result=num1+num2
        replace="addition"
    if operation=="2":
        if num1>num2:
            result=num1-num2
            replace="substraction"
            flag=True
        else:
            print("cannot substract,The first number is less then the second one")
            flag=False
    if operation=="3":
        if num1!=0 or num2!=0:
            result=num1*num2
            replace="multiplication"
        else:
            print("cannot multiply the numbers")
            flag=False
    if operation=="4":
        if num!=0:
            result=num1/num2
            replace="division"
        else:
            print("cannot divide by this number")
            flag=False
    if operation=="5":
        result=num1%num2
        replace="modulus"
    if flag==True:
        print("the ",replace,"between",num1,"and",num2,"is",result)

    again()

def again():
    o=input("do you want to continue\n type y or n")
    if o=="y":
        calc()
    elif o=="n":
        print("Thank you for using the calculator")
    elif o!="y" or o!="n":
        print("enter correct input")
        again()

calc()






