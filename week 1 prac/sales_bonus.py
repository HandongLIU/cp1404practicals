# Handong LIU
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
Normal_Bonus = 0.1
Extra_bonus = 0.15

Sales = float(input("Enter sales:$"))
if Sales >= 1000:
    bonus = Sales * Extra_bonus
else:
    bonus = Sales * Normal_Bonus
print("Bonus is $", bonus, sep='')
sales = float(input("Enter sales: $"))