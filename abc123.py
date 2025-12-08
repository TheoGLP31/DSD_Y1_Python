import csv

FILENAME = "scores.csv"

def add_score(username, score):
    with open("scores.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score])

    pass

def show_scores():
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            print(f"{line[0]} scored {line[1]}.")
    
    pass

def sortDescending():
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        sortedList = {}
        tempLast = 0
        for line in reader:
            print(tempLast)
            if int(line[1]) > tempLast:
                sortedList[sortedList[tempLast] - 1] = int(line[1])
                tempLast = int(line[1])
            else:
                sortedList[sortedList[tempLast] + 1] = int(line[1])
        print(sortedList)

def main():
    while True:
        print("\n1. Add score")
        print("2. Show all scores")
        print("3. Sort Descending")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            score = int(input("Enter score: "))
            add_score(username, score)
        elif choice == "2":
            show_scores()
        elif choice == "3":
            sortDescending()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()