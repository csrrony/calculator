                
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation\n")
print("1.Add\n")
print("2.Subtract\n")
print("3.Multiply\n")
print("4.Divide")

while True:
    choice = input("\nEnter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            print("Your answer is", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            print("Your answer is", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            print("Your answer is", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            print("Your answer is", divide(num1, num2))
        break
    else:
        print("Invalid Input")

print("\t\t----Your process complete----")

        
        

