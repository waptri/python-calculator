def addition(x, y):
    return(x + y)

def subtraction(x, y):
    return(x - y)

def mutiplication(x, y):
    return(x * y)

def division(x, y):
    return(x / y)

def main():
    print("simple calculator")
    print("options: +, -, *, /")
    choice = input("Enter choice:")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if choice == '+':
        print(f"result {add(num1, num2)}")
    elif choice == '-':
        print(f"Result {subtract(num1, num2)}")
    elif choice == '*':
        print(f"results {multiply(num1, num2)}")
    elif choice == '/':
        print(f"result { divide(num1, num2)}") 
    else:
        print("Invalid choice")
                  
    if __name__ == "__main__":
       main()
        



