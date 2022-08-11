num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("Select the operator you want to perform:")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")
print("5 modulus")
operation=input("Please choose an operation from these(1,2,3,4,5):")
if operation=="1":
    result=num1+num2
    replace="addition"
if operation=="2":
    result=num1-num2
    replace="substractiion"
if operation=="3":
    result=num1*num2
    replace="multiplication"
if operation=="4":
    result=num1/num2
    replace="division"
if operation=="5":
    result=num1%num2
    replace="modulus"
print("the ",replace,"between",num1,"and",num2,"is",result)








