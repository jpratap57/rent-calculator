# ask user to enter the amount of rent, food, electricity units, charge per unit and number of people living
rent = int(input("Enter the amount of flat/hostel stay rent: "))
food = int(input("Enter the amount of food expenses you made this month: "))
electricity_units = int(input("Enter the electricity units you've used this month: "))
charge_per_unit = int(input("Enter the charge per unit in your locality: "))
person = int(input("Enter the number of people living in the hostel/flat: "))

total_electricity_bill = electricity_units * charge_per_unit
total_expenses = rent + food + total_electricity_bill

total_money_to_pay = total_expenses // person

print(f"Each person needs to pay: ", total_money_to_pay,"INR.")