# MAIN VARIABLES

BOWLING_LANES = 31

remainingLanes = BOWLING_LANES
takenLanes = []

for i in range(0, BOWLING_LANES):
    takenLanes.append("OPEN")

print(takenLanes)

# FUNCTIONS
# MAIN FUNCTIONS
def checkInt(number):
    final = number
    try:
        number = int(number)
        final = int(number)
    except:
        final = number
    finally:
        return final

def checkStr(string):
    valid = True
    try:
        string = str(string)
        valid = True
    except:
        valid = False
    finally:
        return valid

# CUSTOMER FUNCTIONS
def getPricing():
    6.20 - senior
    7.20 - junior
    
def getLane():
    """
    Checks the given lane number against the takenLanes dictionary, it then returns True or False depending on the result - TRUE if the lane is booked, FALSE if it is taken or a integer has not been inputed
    """

    laneNumber = input(f"There are {remainingLanes} lanes open. What lane number would you like? ")
    valid = True

    laneNumber = checkInt(laneNumber)

    if takenLanes[laneNumber - 1] == "CLOSED":
        valid = False
        print("TAKEN")
    else:
        valid = True
        laneNumber = int(laneNumber) - 1
        takenLanes[laneNumber] = "CLOSED"
        remainingLanes -= 1

    return valid

print(takenLanes)

# MAIN PANEL

while True:
    choice = input("Customer or Staff? ").lower()

    if choice == "customer" or choice == "staff":
        if choice == "customer":
            choice = input("(1) Book a Lane, (2) break")
            if choice == "1":
                print(takenLanes)
                result = getLane()
                while result == False:
                    cont = input("Say 'exit' to stop trying to book a lane. Click ENTER if you want to continue trying. ").lower()
                    if cont == "exit":
                        break
                    getLane()
        else:
            print("b")