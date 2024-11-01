balance = 0
initial_deposit = int(input("enter the initial deposit"))

balance = balance + initial_deposit
salary_credited = int(input("Salary Credited"))
balance = balance + salary_credited
online_purchase = float(input("online purchase"))
balance= balance - online_purchase
house_rent = int(input("House rent should be paid"))
balance-= house_rent
print(balance)