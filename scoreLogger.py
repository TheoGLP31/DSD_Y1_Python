def checkInt(num):
    """
    Checks that num is an integer, returns True if it is an integer, false if not.
    """

    try:
        num = int(num)
        return True
    except:
        return False

scoreValid = False
filterValid = False

while True:
    choice = input("Would you like to: (1) Add another name, (2) View all scores, (3) Filter scores by number, (4) Stop ")

    if choice == "1":
        with open("scores.txt", "a") as file:
            name = input("Enter your name: ")
            while scoreValid == False:
                score = input("Enter score: ")
                scoreValid = checkInt(score)
            
                file.write(f"{name}: {score} \n")

    if choice == "2":
        with open("scores.txt", "r") as file:
            for line in file:
                print(line.strip())

    if choice == "3":
        toFilter = input("What number would you like to sort by? ")
        while filterValid == False:
            filterValid = checkInt(toFilter)

        toFilter = int(toFilter)
        with open("scores.txt", "r") as file:
            for line in file:
                newLine = line.split()
                newLine[1] = int(newLine[1])
                if newLine[1] == toFilter:
                    print(line.strip())
    
    if choice == "4":
        break