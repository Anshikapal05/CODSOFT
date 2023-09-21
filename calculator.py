# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def main():
    print("====================================\n")
    print("             CALCULATOR")
    keep_going = True
    while keep_going:
        print("\n====================================")
        print("\n\nOperations Available are:-\n")
        print("1. Addition(+)\n2. Subtraction(-)\n3. Multiplication(*)\n4. Division(/)\n5. EXIT\n\n ")
        choice = input("Enter operation (1/2/3/4/5) : ")
        if choice == "5":
            print("\nThank You!\n")
            keep_going = False
        else:
            
            num1 = float(input("\n\nEnter first number: "))
            num2 = float(input("\nEnter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print("\nRESULT:   ", result)
            elif choice == '2':
                result = subtract(num1, num2)
                print("\nRESULT:   ", result)
            elif choice == '3':
                result = multiply(num1, num2)
                print("\nRESULT:   ", result)
            elif choice == '4':
                result = divide(num1, num2)
                print("\nRESULT:   ", result)
            else:
                print("\nInvalid input. Please choose a valid operation.")

if __name__ == "__main__":
    main()