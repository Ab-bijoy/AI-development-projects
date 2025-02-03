# Addtion function
def add (x,y):
    return x+y


# Subtration function
def sub (x,y):
    return x-y

# Multiplication function
def multiplx (x,y):
    return x*y
# Division function
def division (x,y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x/y
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("Enter choices (1/2/3/4) : ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice=='1':
                print(num1,"+",num2,"=",add(num1,num2))
            elif choice=='2':
                print(num1,"-",num2,"=",sub(num1,num2))
            elif choice=='3':
                print(num1,"*",num2,"=",multiplx(num1,num2))
            elif choice=='4':
                print(num1,"/",num2,"=",division(num1,num2))
        
        next_calculation = input("Do you want to perform another calculcation?(yes/no)")
        if next_calculation.lower() != 'yes':
            break
        print("Exiting Calculator.")
    
calculator()