def labResultsConverter():
    mgdlTommoll = 0.0555
    mmollTomgdl = 18.018

    def convert(toConvert ,convertTo):
        num = toConvert

        if convertTo.lower() == "mmol/l":
            newNum = num * mgdlTommoll
        else:
            newNum = num * mmollTomgdl
        
        return newNum

    number = float(input("Give the value: "))
    typeConvert = str(input("Give the type you want to convert to (mmol/l or mg/dl): "))

    if typeConvert:
        if typeConvert.lower() == "mmol/l" or typeConvert.lower() == "mg/dl":
            newNum = convert(number, typeConvert)

            print(f"{number}{"mmol/l" if typeConvert.lower() == "mg/dl" else "mg/dl"} is {round(newNum, 3)}{typeConvert.lower()}")
        else:
            print(f"Your type to convert to is incorrect, you put '{typeConvert}', it needs to be 'mg/dl' or 'mmol/l'.")

def averageTemperatureTracker():
    temps = []

    totalTemp = 0

    IMP_MIN = 30
    IMP_MAX = 45

    MAX_TEMP = 38

    for i in range(3):
        newTemp = float(input(f"Please enter temperature reading #{i + 1}: "))
        temps.append(newTemp)
        totalTemp += newTemp

    average = round(totalTemp / len(temps), 2)

    if average >= IMP_MAX or average <= IMP_MIN:
        print("stop being stupid. honestly.")
    elif average >= MAX_TEMP:
        print(f"💀⚠️ Your average temperature is in the fever threshold at {average}°C. The highest non-fever threshold temperature is 45°C. ⚠️💀")
    else:
        print(f"Your average temperature is {average}°C. This is {round(MAX_TEMP - average, 2)}°C below the highest non-fever threshold temperature.")

def heartRateMonitor():
    age = int(input("What is your age? "))
    restingHeartRate = int(input("What is your resting heart rate? "))
    MAX_HEART_RATE = 220
    safeMax = MAX_HEART_RATE - age

    NORMAL_HR_MIN = 60
    NORMAL_HR_MAX = 100

    print(f"Your safest maximum heart rate is {safeMax}. Your resting heart rate is {"Low" if restingHeartRate <= NORMAL_HR_MIN else "Normal" if restingHeartRate <= NORMAL_HR_MAX and restingHeartRate >= NORMAL_HR_MIN else "High"}")

def waterIntakeCalc():
    waterIntake = float(input("Input water intake (ml): "))

    DAILY_GOAL = 1600

    overOrUnder = abs(waterIntake - DAILY_GOAL)

    print(f"You drank {waterIntake}ml of water, the daily goal is {DAILY_GOAL}ml. You did {"not " if waterIntake < DAILY_GOAL else ""}reach the daily water intake goal. You drank {overOrUnder if overOrUnder >= 0 else (overOrUnder + DAILY_GOAL)}ml {"more than" if waterIntake - DAILY_GOAL >= 0 else "less than"} the daily intake")