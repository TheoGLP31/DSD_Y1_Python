name = "Alex"

def change_name():
    name = "Jordan"
    print("Inside function:", name)
    return name

newName = change_name()
print("Outside function:", newName)