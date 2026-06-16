print("Welcome To The Print Calculator")

total_bill = float(input("What was the total bill? "))
tip = int(input("How much tip would would you like to give 10, 12 or 15 ? "))
split_bill = int(input("How many people to split the bill? "))

each_person_pay = round((total_bill + tip ) / (split_bill))

print(f"Each person should pay. ${each_person_pay}")