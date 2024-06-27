# summation of 2 numbers
def add(a, b):
    return a + b

# subtraction of two numbers
def subtract(a, b):
    return a - b

# multiplication two numbers
def multiply(a, b):
    return a * b

# division of two numbers
def divide(a, b):
    return a / b


print("Select operation.")
print("1.Summation")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    # take input from the user as user's requirement
    choice = input("Enter choice(1/2/3/4): ")

    # check your choice 
    if choice in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter 1st number: "))
            n2 = float(input("Enter 2nd number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif choice == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif choice == '4':
            print(n1, "/", n2, "=", divide(n1, n2))
        
        # get user's choice as requirement for continue or break the loop
        # continue loop,if answer is yes
        # break loop, if answer is no
        next_calculation = input("Do you want to do more calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")