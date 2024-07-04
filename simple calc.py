def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def main():
    print("simple calculator")
    print("options: +, -, *, /")
    choice = input("Enter choice: ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '+':
        print(f"result: {add(num1, num2)}")
    elif choice == '-':
        print(f"result: {subtract(num1, num2)}")
    elif choice == '*':
        print(f"result: {multiply(num1, num2)}")
    elif choice == '/':
        print(f"result: {divide(num1, num2)}") 
    else:
        print("Invalid choice") 
                   
    if __name__ == "__main__":
      main()      
   