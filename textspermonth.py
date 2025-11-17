username = input("Input your name pls") 
MobilePhone = input("Input your number pls") 
UserMinutes = float(input("How many minutes have you used this month?") )

minutesThisMonth = UserMinutes * 0.10

UserTexts = int(input("How many texts have you sent pls?"))

textsThisMonth = UserTexts * 0.05

total = minutesThisMonth + textsThisMonth

vat = total * 1.20

print(total)
print(total + vat)