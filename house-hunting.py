annual_salary = float(input('Enter your annual salary: '))
percent_of_salary = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

current_savings = 0
months_to_down = 0
r = .04

while current_savings < (total_cost * .25):
    monthly_savings = (annual_salary * percent_of_salary / 12) + (current_savings * r / 12)
    current_savings += monthly_savings
    months_to_down += 1 

print(months_to_down)

