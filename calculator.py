while True:
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers!")
        continue

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero!")
    else:
        print("Invalid choice!")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using the calculator!")
        break