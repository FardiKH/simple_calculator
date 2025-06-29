print("Script created by Fardi Khalilov")

print("Welcome to the Simple Calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose operations:")
print("1.add (+)")
print("2.subtract (-)")
print("3.multiply (*)")
print("4.divide (/)")

choice = input("Enter choice (1/2/3/4): ").strip()

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
    print("Invalid operation selected!")