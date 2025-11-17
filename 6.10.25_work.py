import random as rand

def area():
    """
    Calculates the area of a rectangle and rounds to 2 digits
    
    Inputs:
    - Length
    - Width

    Output:
    Print statement, rounds to 2 digits
    """
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    print(round(length * width, 2)) # Calculates the area

def minutesToHours():
    """
    Converts minutes to hours and minutes

    Inputs:
    - Minutes

    Outputs:
    Print statement
    """
    minutes = int(input("Enter the time in minutes: "))

    print(f"{minutes} minutes is {minutes // 60}h {minutes % 60}m") # Calculate the hours and then the minutes

def VAT():
    """
    Adds VAT to a bill and rounds it to 2 places

    Inputs:
    - Total Price

    Outputs:
    Print statement
    """
    totalPrice = float(input("Enter the total price: £"))

    print(f"With VAT your total price is: £{round(totalPrice * 1.2, 2)}") # Times the total price by 1.2 to get 20% more and then rounds it to 2 decimal places

def hospitalBill():
    """
    Gets the patient's name, age, and total bill, checks if patient is younger than 18, if they are, applies a 5% discount, prints 
    total bill and then if total is over £1000 it will ask if they want to join their payment plan, if yes it will print the monthly bill

    Inputs:
    - Patient Name
    - Patient Age
    - Bill Amount

    Outputs:
    Print statement x3 (Prints out total bill, asks if they want to join the payment plan if over £1,000, prints out the total bill per month if payment plan is yes.)
    """
    patientName = input("Enter patient's name: ")
    patientAge = int(input("Enter patient's age: "))
    billAmount = (float(input("Enter patient's bill amount: £")) * 1.2)

    if patientAge < 18:
        billAmount = billAmount * 0.95 # Applys a 5% discount
    
    print(f"{patientName}'s bill amount {"with the 5% discount for being under 18 " if patientAge < 18 else ""}is £{round(billAmount, 2)}") # Print out the patient's name, message if they have recieved the discount and their total bill rounded to 2 decimal places

    if billAmount > 1000:
        paymentPlan = input(" ! Your bill is greater than £1,000 you can join our 12 month payment plan. ! ") # Offers payment plan if bill is greater than 1000

        if paymentPlan == "Yes":
            print(f"The monthly payment bill is: £{round(billAmount / 12, 2)}")
        else:
            print("okay")

def passwordChecker():
    """
    Checks if the password is the correct one

    Inputs:
    - Password

    Outputs:
    Print statement
    """
    correctPassword = rand.randint(1, 10)

    correct = False

    while correct == False:
        password = int(input("Enter password: "))
        if password == correctPassword:
            print("Correct password")
            correct = True
        elif password == "____":
            print(correctPassword)
        else:
            print("Try again! 😡")

def patientMenu():
    patientName = input("Enter patient's name: ")
    patientAge = input("Enter patient's age: ")
    
    selection = int(input("Enter selection: (1) BMI Calculator, (2) Dosage Tracker, (3) Exit"))

    if selection == 1:
        print("-insert old BMI calculator-")
    elif selection == 2:
        print("-insert old dosage tracker-")
    else:
        next

while True:
    choice = input("(1) Area, (2) Minutes to Hours, (3) VAT, (4) Hospital Billing, (5) Password Checker, (6) Patient Menu, or enter nothing to exit ") # Asks what program to run

    if choice == "1":
        help(area)
        area() # Runs Area
    elif choice == "2":
        help(minutesToHours)
        minutesToHours() # Runs MinutesToHours
    elif choice == "3":
        help(VAT)
        VAT() # Runs VAT
    elif choice == "4":
        help(hospitalBill)
        hospitalBill() # Runs HospitalBill
    elif choice == "5":
        help(passwordChecker)
        passwordChecker() # Runs PasswordChecker
    elif choice == "6":
        patientMenu()
    else:
        print("Exitting...")
        break