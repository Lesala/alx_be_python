#Prompting the user to enter their monthly income
monthly_income = float(input("Enter your monthly income: "))
#Prompting the user to enter their monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))
# calculating the monthly savings
monthly_savings = monthly_income - monthly_expenses 
#calculating projected savings over one year
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Displaying the user's monthly savings and projected annual savings
print(f'Your monthly savings are ${monthly_savings:.2f}')
print(f'Your projected savings after one year, including a 5% interest, is ${Projected_savings:.2f}')
