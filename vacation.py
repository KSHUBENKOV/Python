name = input("Please enter your name ")
age = int(input("Please enter your age "))

if age > 18 and age < 31:
    print("welcome to your holiday vacation, {0}!".format(name))
else:
    print("You shall not pass!")
