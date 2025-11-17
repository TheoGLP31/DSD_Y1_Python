"""
glucose = 7.0

if glucose > 7.0:
    print("high")
else:
    print("low")

oxygen = 90

if oxygen > 95:
    print("low")
else:
    print("high")

heartrate = 70

if heartrate == 70:
    print("good")
else:
    print("bad")
"""

def tempCheck(temp):
    if temp > 37.5:
        return "High"
    elif temp == 37.5:
        return "Normal"
    else:
        return "Low"
    
def heartRateCheck(hr):
    if hr >= 60 and hr <= 100:
        return "Normal"
    elif hr < 60:
        return "Low"
    else:
        return "High"
    
def oxygenCheck(o2):
    if o2 >= 95:
        return "Normal"
    else:
        return "Low"

def task3():
    dayData = []

    def getCount(dayData):
        dayData = dayData + [0] + [0]

        monday = int(input(f"Input your step count for Monday: "))
        friday = int(input(f"Input your step count for Friday: "))

        return monday, friday

    day0, day1 = getCount(dayData)

    if day0 < day1:
        print("Increased")
    else:
        print("Decreased")

while True:                                            
    choice = int(input("(1) Temperature Check, (2) Heart Rate Check, (3) Oxygen Check, (4) Step Count Comparison, (5) Exit "))

    if choice == 1:
        temp = float(input("Give temp: "))
        tempResult = tempCheck(temp)

        print(f"Your temperature is {tempResult}")
    elif choice == 2:
        heartRate = int(input("Give heart rate: "))
        tempResult = heartRateCheck(heartRate)

        print(f"Your heart rate is {tempResult}")
    elif choice == 3:
        oxygen = int(input("Enter oxygen (%): "))
        tempResult = oxygenCheck(oxygen)

        print(f"Your oxygen level is {tempResult}")
    elif choice == 4:
        task3()
    else:
        break