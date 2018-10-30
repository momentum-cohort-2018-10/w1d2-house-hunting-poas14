# Call the cost of your dream home total_cost​.
# Call the portion of the cost needed for a down payment portion_down_payment​. For simplicity, assume that portion_down_payment = 0.25 (25%).
# Call the amount that you have saved thus far current_savings​. You start with a current savings of $0.
# Assume that you invest your current savings wisely, with an annual return of r ​(in other words, at the end of each month, you receive an additional current_savings*r/12​ funds to put into your savings – the 12 is because r​ is an annual rate). Assume that your investments earn a return of r = 0.04 (4%).
# Call your annual salary annual_salary​.
# Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that portion_saved​. This variable should be in decimal form (i.e. 0.1 for 10%).
# At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary ​(annual salary / 12).

annual_salary = float(input('Enter your annual salary: '))
percent_of_salary = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

current_savings = 0
months_to_down = 0
r = .04

while current_savings < (total_cost * .25):
    monthly_savings = ((annual_salary * percent_of_salary) / 12) + (current_savings * r / 12)
    current_savings += monthly_savings
    months_to_down += 1 

print(months_to_down)