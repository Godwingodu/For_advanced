num1=int(input("Enter the first number:-"))
num2=int(input("Enter the second number:-"))
print("Enter the operation you want to perform")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
operation=int(input("choose an option from these (1,2,3,4,5): "))
while(operation==1):
    sum=num1+num2
    print("sum is",sum)
    exit()
while(operation==2):
    dif=num1-num2
    print("Difference is",dif)
    exit()
while(operation==3):
    mul=num1*num2
    print("Multiplication is",mul)
    exit()
while(operation==4):
    div=num1/num2
    print("Division is",div)
    exit()
while(operation==5):
    mod=num1%num2
    print("Modulus is",mod)
    exit()

