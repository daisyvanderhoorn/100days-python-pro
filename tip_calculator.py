print("Welcome to the tip calculator!")


# Simple solution without try/catch block for input types
bill = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_percentage /= 100
total_bill = bill * (1 + tip_percentage)
print(f"Total bill with tip is €{round(total_bill, 2)}")

amount_of_people = int(input("How many people are we splitting the bill with? "))
total_bill_split = total_bill / amount_of_people

print(f"Each persons should pay €{round(total_bill_split, 2)}")
