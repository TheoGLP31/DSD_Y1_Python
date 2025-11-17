machines = ["Pinball Wizard", "Dance Floor X", "Retro Racer", "Alien Blaster"]
categories = ["Pinball", "Rhythm", "Racing", "Shooter"]
status = ["Working", "Working", "Needs Service", "Working"]

while True:
    choice = input("(1) View all machines, (2) Add a machine, (3) Update status, (4) Filter by category, (5) List machines needing service, (6) Exit ")

    if choice == "1":
        for i in range(len(machines)):
            print(f"#{i + 1} - {machines[i]}")
    elif choice == "2":
        newMachine = input("Enter machine name: ")
        newCategory = input(f"Enter {newMachine} category: ")
        newStatus = input(f"Enter {newMachine} status: ")

        machines.append(newMachine)
        machines.append(newCategory)
        machines.append(newStatus)