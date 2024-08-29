def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

while True:
    option  = input("Enter which operation you want to perform [add,substract,multiply, divide,quit]" ).lower()
    num1 = int(input("Enter the first number "))
    num2 = int(input("Ente the second number"))

    if option == "add":
        print(f"Result : {add(num1,num2)}")
    elif option == "substract":
        print(f"Result :{substract(num1,num2)}")
    elif option == "multiply":
        print(f"Result :{multiply(num1,num2)}")
    elif option == "divider":
        print(f"Result :{substract(num1,num2)}")
    elif option == "quit":
        break