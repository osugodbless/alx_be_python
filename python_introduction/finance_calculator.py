# Prompt user for monthly income and total monthly expenses
monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expense

# Project annual savings
interest_rate = 0.05        #Assuming the interest rate is 5%
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

print("Your monthly savings are $", monthly_savings)
print("""Projected savings after one year, with interest, is: $""", projected_savings)
