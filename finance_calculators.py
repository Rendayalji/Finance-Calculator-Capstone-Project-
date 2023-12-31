
'''This Finance calculator Capstone Project task involves setting up a
program that gives the user choice therefore if, elif and else 
conditions will be used.

1.  Display investment and bond calculator options for the user to 
    select from. 
    Note to change user entry to lowercase so their selection does not
    affect how the program proceeds.

2.  Set up 'if condition' for investment calculator followed by 
    questions requesting the user for data.
    
2a. Within the if investment condition, set up if, elif 
    conditions to calculate and then print simple interest or compound 
    interest using the simple and compound interest formulas, else will 
    be used for an invalid entry.

3. Set up elif condition for bond calculator followed by questions 
   requesting the user for data.
   Use the repayment formula and print the amount to repay each month.

4. Set else condition for user entry that is not investment or bond.
'''
import math

# The user will see the following calculation options:
print(
"investment - to calculate the amount of interest you'll earn on \
your investment."
)

print(
"bond       - to calculate the amount you will have to pay on a \
home loan.\n"
)

# User first asked to enter their calculation option.
calculation_option = input("Please enter either 'investment' or 'bond' from \
the menu above to proceed: \n").lower()
print("\n")

# If the user selects investment, a number of questions will follow.
# User asked to input data for the investment calculation.
if calculation_option == "investment":
    print("You have selected the investment calculator:\n")
    deposit = float(input("Please enter the amount of money to deposit: \n"))
    print(f"Deposit: £{deposit} \n")
    
    interest_rate = float(input("Please enter the interest as a percentage:  \n"))
    print(f"Interest rate: {interest_rate}%\n")
    
    total_years = int(input("Please enter the number of years that you plan \
on investing: \n"))
    print(f"Number of years: {total_years} years \n")
    
    interest = input("Please enter 'simple' or 'compound' interest: \n").lower()
    

    P = deposit
    r = (interest_rate) / 100
    t = total_years
    
    # Formula to calculate the total amount when simple interest applied:
    amount_with_simple = P *(1 + r*t)
    
    # Formula to calculate the total amount when compound interest applied:
    amount_with_compound = P * math.pow((1+r),t)
    
    if interest == "simple":
        print(f"\nThe total amount you will earn after simple interest: \
£ {amount_with_simple:.2f}")
    elif interest == "compound":
        print(f" \nThe total amount you will earn after compound interest: \
£ {amount_with_compound:.2f}")
    else:
        print("This is an invalid entry.  Please enter either 'simple' or \
'compound'.")
        
    
# If the user selects bond, a number of questions will follow.
# User asked to input data for the bond repayment calculation.

elif calculation_option == "bond":
    print("You have selected the bond calculator.\n")
    
    present_value_of_house = float(input("Please enter the present value of \
your house: ")) 
    print(f"Present value of house: £{present_value_of_house}\n") 
    
    interest_rate = float(input("Please enter the interest as a percentage: "))
    print(f"Interest rate: {interest_rate}%")
    
    monthly_interest_rate = float((interest_rate / 100) / 12)
    print(f"Monthly interest rate: {monthly_interest_rate} % \n")
    
    months_to_repay = int(input("Please enter the number of months to repay: "))
    print(f"Number of months to repay: {months_to_repay} months \n")
    
    i = monthly_interest_rate
    P = present_value_of_house
    n = months_to_repay
    
    # Formula for monthly repayment on a home loan.
    repayment = (i * P)/(1 - (1 + i)**(-n))
    
    print(f"The amount of money you to repay each month: £{repayment:.2f}") 
    
# User does not input investment or bond, an error message will be output.
else:
    print(
"investment - to calculate the amount of interest you'll earn on \
your investment."
)
    
    print(
"bond       - to calculate the amount you will have to pay on a \
home loan.\n"
)
    
    print(
"Invalid entry. Please enter either investment or bond from the \
above menu to proceed."
)
    