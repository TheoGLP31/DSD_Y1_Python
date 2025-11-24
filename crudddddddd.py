totalLoans = 100

def create():
    global totalLoans

    file = open("data.txt", "a")
    loadId = totalLoans + 1
    totalLoans += 1
    studentName = input("Enter your full name: ")
    studentID = input("Enter your student ID: ")
    deviceType = input("What is the type of device? ")
    device_id = "L-" + ("00" if totalLoans < 10 else "0" if totalLoans < 100 else "") + str(totalLoans)
    dateOut = input("Enter the date it was given (YYYY/MM/DD): ")
    dateSplit = dateOut.split("/")
    dueBack = str(dateSplit[0]) + "/" + str(int(dateSplit[1]) + 1) + "/"  + str(dateSplit[2])
    returned = bool(input("Has it been returned? [True or False]"))
    dictionary = {
        "loan_id": loadId,
        "student_name": studentName,
        "student_id": studentID,
        "device_type": deviceType,
        "device_id": device_id,
        "date_out": dateOut,
        "due_back": dueBack,
        "returned": returned
    }
    file.write(str(dictionary.keys()) + str(dictionary.values()))
    file.close()

create()