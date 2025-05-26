years_of_experience = int(input("Enter the employee's years of experience: "))
age = int(input("Enter the employee's age: "))

if years_of_experience > 25 and age >= 55:
    atr = 5600000
elif years_of_experience > 20 and age >= 45:
    atr = 4480000
elif years_of_experience > 10 and age >= 35:
    atr = 1500000
else:
    atr = 550000

# Print the result
print(f"The Annual Tax Revenue (ATR) for this employee is: {atr}")
