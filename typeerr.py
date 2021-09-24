first_number = float(input("What is your first number?"))
# Ask the user what the first number is before calculation.
second_number = float(input("What is your second number?"))
# Ask the user the second number.
cal = str(
    input(
        "Do you want to add, subtract, multiply, or divide? You can also square, or calculate with each option."
    )
)
if cal == "add":
    print(f"Done! The result is {first_number + second_number}")
    # Checks if the user wants to add, then adds if so. Then prints the final number.
if cal == "subtract":
    print(f"Done! The result is {first_number + second_number}")
    # Divides and prints.
if cal == "multiply":
    print(f"Done the result is {first_number * second_number}")
    # Multiplies
if cal == "square":
    print(f"Done! The result is {first_number * second_number}")
if cal == "divide":
    print(f"Done! The result is {first_number / second_number}")
    remainder = str(
        input(
            "Assuming you know the original number, would you like to see the integer remainder? (y/n)"
        )
    )
    if remainder == "y":
        print(f"Here you go. The result is {first_number % second_number}")
