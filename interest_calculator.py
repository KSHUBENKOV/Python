principal = float(input("Enter principal amount: "))

rate = float(input("Enter rate of interest: "))

time = float(input("enter time (in years): "))

interest = (principal * rate * time) / 100

print(f"Simple interest is: {interest}")
