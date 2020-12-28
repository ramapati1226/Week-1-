def check_mul(num1,num2):
    if(num1%num2==0):
        print(num1,"is multiple of",num2)
    else:
        print(num1,"is not multiple of",num2)
num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
check_mul(num1,num2)
