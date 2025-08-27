# Enhanced Basic Calculator Program

while True:
    print("\n--- Simple Python Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        continue

    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("❌ Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("❌ Invalid operation. Use +, -, *, or /.")

    # Ask the user if they want to continue
    again = input("\nWould you like to calculate again? (yes/no): ").lower()
    if again != 'yes':
        print("✅ Thank you for using the calculator. Goodbye!")
        break
