machines = {
    "Pinball Wizard":{"category":"Pinball", "status":"Working"}, 
    "Dance Floor X":{"category": "Rhythm", "status":"Working"},
    "Retro Racer":{"category":"Racing", "status":"Needs Service"},
    "Alien Blaster":{"category": "Shooter", "status":"Working"},
}

while True:
    choice = input("(1) View all machines, (2) Add a machine, (3) Update status, (4) Filter by category, (5) List machines needing service, (6) Exit ")

    if choice == "1":
        print(machines)
    elif choice == "2":
        newMachine = input("Enter machine name: ")
        newCategory = input(f"Enter {newMachine} category: ")
        newStatus = input(f"Enter {newMachine} status: ")

        newDict = {"category":newCategory, "status":newStatus}

        machines[newMachine] = newDict
    elif choice == "3":
        machine = input("Enter machine name: ")
        newStatus = input("(1) Working, (2) Needs Service, (3) Not Working ")

        status = "Working" if newStatus == "1" else "Needs Service" if newStatus == "2" else "Not Working"
        machines[machine]["status"] = status
    elif choice == "4":
        category = input(f"Choose a category: ")
        filteredList = []

        for i in range(len(machines)):
            machineName = list(machines.keys())[i]

            if machines[machineName]["category"] == category:
                filteredList.append(machineName)
            else:
                continue
        
        print(filteredList)
    elif choice == "5":
        serviceList = []

        for i in range(len(machines)):
            machineName = list(machines.keys())[i]

            if machines[machineName]["status"] == "Needs Service":
                serviceList.append(machineName)
            
        print(serviceList)
    elif choice == "6":
        break
    else:
        print("t")