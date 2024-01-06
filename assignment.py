def classify_number(num):
    if num < 0:
        print("The number is negative.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")

number = int(input("Enter a number: "))
classify_number(number)
