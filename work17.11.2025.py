energyLevels = [1, 2, 3, 4, 5]
usernames = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]
values = [4235, 7546, 1243, 6425, 9412, 15431]

for i in range(len(energyLevels)):
    print(energyLevels[i])

for i in range(len(usernames)):
    print(usernames[i])

for i in range(len(values)):
    print(values[i])

print("First Values")
print(energyLevels[0])
print(usernames[0])
print(values[0])

print("Middle Values")
print(energyLevels[len(energyLevels) // 2])
print(usernames[len(usernames) // 2])
print(values[len(values) // 2])

print("Last Values")
print(energyLevels[len(energyLevels) - 1])
print(usernames[len(usernames) - 1])
print(values[len(values) - 1])