import math
import random
from datetime import datetime
import numpy

def check_int(number):
    try:
        number = float(number)
        return number
    except:
        return ""

flag = True

def main_menu():
    choice = input("(1) Math Module, (2) Random Module, (3) Datetime Module, (4) Numpy Module (5) All Modules ")
    if choice == "1":
        while flag:
            numbers = check_int(input("Enter pls: "))
            if numbers == "":
                print("no.")
                flag = True
            else:
                print(f"Square Root: {round(math.sqrt(numbers), 2)}")
                print(f"Exp: {round(numbers ** 2, 2)}")
                print(f"Round Up: {round(math.ceil(numbers), 2)}")
                print(f"Round Down: {round(math.floor(numbers), 2)}")
                print(f"Area of a circle with inputted number as radius: {(round(math.pi * (numbers ** 2)), 2)}")
    elif choice == "2":
        lives = 3
        
        round_tracking = {}
        
        tries = 0

        while lives != 0:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            total = dice1 + dice2

            print(f"Dice 1: {dice1}\nDice 2: {dice2}\nTotal: {dice1 + dice2}")
            if total == 7 or total == 11:
                print("You Win!")
                round_number = len(round_tracking) + 1
                round_tracking["round_" + str(round_number)] = (tries / 3)
                print(round_tracking)
                break
            else:
                input("Try Again")
                lives -= 1
                tries += 1
    elif choice == "3":
        date = datetime.now().date().strftime("%d/%m/%Y")
        year = date.split("/")[2]
        dob = input("Enter Birth Date (e.g., DD/MM/YYYY): ")
        birth_year = dob.split("/")[2]
        birth_day = dob.split("/")[0]

        age = int(year) - int(birth_year)

        month_days = [31, 28, 31, 30, 30, 31, 31, 30, 31, 30, 31]

        days_till_month = ((month_days[int((date.split("/")[1])) - 1]) - int(date.split("/")[0]))

        print((month_days[int((date.split("/")[1])) - 1]))
        print(int(date.split("/")[0]))

        print(f"Age: {age}")
        print(f"Number of Days till next birthday: {days_till_month}")
    elif choice == "4":
        weekly_sales = numpy.array([120, 135, 150, 98, 175, 200, 143]).astype(float)
        print(f"Mean: {round(numpy.mean(weekly_sales), 2)}\nTotal: {numpy.sum(weekly_sales)}\nHighest: {numpy.max(weekly_sales)}\nLowest: {numpy.min(weekly_sales)}")
        weekly_sales *= 1.1
        print(weekly_sales)
    elif choice == "5":
        array = []
        for i in range(1, 100):
            ran_num = random.randint(1, 100)
            array.append(ran_num)
        array = numpy.array(array)

        mean_array = math.floor(array.mean())

        print(f"Today's Date: {datetime.now().date().strftime("%d/%m/%Y")}\nRandom Number: {mean_array}")

main_menu()