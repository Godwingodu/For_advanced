num1=int(input("Enter the first number:-"))
num2=int(input("Enter the second number:-"))
print("Enter the operation you want to perform")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
operator=int(input("choose an option from these (1,2,3,4,5): "))
if operator==1:
    print("The addition between two number is",num1+num2)
if operator==2:
    print("The substraction between two number is",num1-num2)
if operator==3:
    print("The multiplication between two number is",num1*num2)
if operator==4:
    print("The division between two number is",num1/num2)
if operator == 5:
        print("The modulud between two number is", num1%num2)