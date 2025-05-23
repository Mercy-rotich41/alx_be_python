# Prompt for user inputs
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate savings
monthly_savings = income - expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings * 1.05  # Apply 5% interest

# Output results
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
