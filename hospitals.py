def EHR():
    patients = [0]

    def createPatient():
        patient_name = input("Input patients name: ")
        patient_age = int(input("Input patients age: "))
        patient_dob = str(input("Input patient DOB: "))
        patient_height = float(input("Input patients height: "))
        patient_details = str(input("Input patient information: "))

        newPatient = {
            "name":patient_name,
            "age":patient_age,
            "dob":patient_dob,
            "height":patient_height,
            "info":patient_details
        },

        patients.append(newPatient)

        return patient_name, patient_age, patient_dob, patient_height, patient_details
    
    patient_name, patient_age, patient_dob, patient_height, patient_details = createPatient()

    def findPatient(name, age, dob):#
        for patient in patients:
            if patient["name"].lower() == name.lower():
                print("yay")
    
    findPatient(patient_name, patient_age, patient_dob)

def BMICalculator():
    """
    Calculate BMI pls

    use weight and height pls thanks
    """

    weight = float(input("give weight (kg) "))
    height = float(input("give height (m) "))

    if weight and height:
        BMI = weight / (height * height)

        if BMI <= 1 and BMI >= 0:
            BMI_Category = "STUPID"
            print(f"stop being stupid you absolute BMI category of {BMI, BMI_Category}")
        elif BMI < 18.5 and BMI > 1:
            BMI_Category = "UNDER"
            print(f"You have BMI of {BMI} and you are underweight")
        elif BMI < 24.9:
            BMI_Category = "NORM"
            print(f"You have BMI of {BMI} and you are a normal/healthy weight")
        elif BMI < 29.9:
            BMI_Category = "OVER"
            print(f"You have BMI of {BMI} and you are overweight")
        elif BMI < 39.9:
            BMI_Category = "OB"
            print(f"You have BMI of {BMI} and you are obese")
        else:
            BMI_Category = "MOR_OB"
            print(f"You habe BMI of {BMI} and you are morbidly obese")
        
        print(BMI_Category)

def dosageTracking():
    PATIENT_DOSAGE_DAY = int(input("Patient paracetamol dosage per day (mg): "))

    if PATIENT_DOSAGE_DAY <= 1000:
        print("safe")
    else:
        print("STOP no take anymore you are NOT safe but if you want to go ahead yk? :) free will and such")

def billing():
    roomChargeSET = 3025
    treatmentChargeSET = 28000
    consultationChargeSET = 200

    keep = True

    while keep:
        name = str(input("give name "))
        room = int(input("How many days were you in the room? "))

        roomCharge = room * roomChargeSET

        treatment = int(input("How many times were you treated, e.g. physical therapy? "))

        treatmentCharge = treatment * treatmentChargeSET

        consultation = int(input("how many times were you consulted on please? "))

        consultationCharge = consultation * consultationChargeSET

        totalCharge = roomCharge + treatmentCharge + consultationCharge
        totalWithVAT = totalCharge * 1.2
        VAT = (totalCharge * 1.2) - totalCharge

        print(f"{name}'s bill is £{totalWithVAT} with VAT and VAT is {VAT}")

total_patients = 0

def add_patient(total_patients):
    total_patients += 1

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print("Patient added:", name)

    return total_patients

def view_total():
    global total_patients
    print("Total patients:", total_patients)

def clear_total(total):
    total = 0

    return total

while True:
    choice = input("what run? ")

    if choice == "EHR":
        EHR()
    elif choice == "BMICalc":
        BMICalculator()
    elif choice == "DosageTracking":
        dosageTracking()
    elif choice == "AddPatient":
        total_patients = add_patient(total_patients)
    elif choice == "ViewTotal":
        view_total()
    elif choice == "Billing":
        billing()
    elif choice == "ClearTotal":
        total_patients = clear_total(total_patients)
    else:
        break