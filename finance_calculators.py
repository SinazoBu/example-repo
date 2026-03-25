import math

# Allow user to choose which calculations they want to do

print("Investment - to calculate the amount of interest you will earn.")
print("Bond - to calculate the amount you will have to pay on home loan.")

user_choice = input("Enter 'Investment' or 'Bond': ").lower()

# If user selects investment
# ask user for values

if user_choice == "investment":

    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate(%): "))
    years = int(input("Enter the number of years you plan to invest: "))

    interest = input("Enter 'simple' or 'compound': ").lower()
    r = interest_rate / 100

    # Formular for simple
    if interest == "simple":
        total_amount = deposit * (1 + r * years)

    # Formular for coumpond
    elif interest == "compound":
        total_amount = deposit * math.pow((1 + r), years)

    else:
        print("Invalid Interest type. Please enter 'simple' or 'compound'.")
        exit()

    print(f"Total amount after {years} years : R{total_amount:.2f}")

# If user selects bond
# Ask user for values

elif user_choice == "bond":

    present_value = float(input("Enter present value of the house: "))
    interest_rate_bond = float(input("Enter Interest rate(%): "))
    number_of_months = int(input("Enter number of months to repay: "))

    i = (interest_rate_bond / 100) / 12

    total_repayment = (i*present_value)/(1-(1 + i) ** (-number_of_months))

    print(f"Your monthly repayment will be: R{total_repayment:.2f}")

else:
    print("Please enter a valid option ('investment' or 'bond'.)")
