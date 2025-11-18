listA = [1, 2, 3]
listB = [1, "2", 3.0]

print(listA)
print(listB)

print(type(listA[2]))
print(type(listB[1]))
print(type(listB[2]))

notifications = [34, 28, 55, 40, 60, 22, 18]

total = 0

for i in range(len(notifications)):
    total += notifications[i]

print(f"\n Highest: {max(notifications)} \n Lowest: {min(notifications)} \n Total: {total} \n Average: {round(total / len(notifications))}")
newValue = int(input("Enter number: "))
notifications.append(newValue)
print(f"Updated List: {notifications}")

notifications2 = [42, 45, 12, 6, 9, 87, 0]

print(f"\n User 1: {notifications} \n User 2: {notifications2}")
print(f"\n User 1: \n Highest: {max(notifications)} \n Lowest: {min(notifications)} \n Total: {sum(notifications)} \n Average: {round(sum(notifications) / len(notifications))} \n User 2: \n Highest: {max(notifications2)} \n Lowest: {min(notifications2)} \n Total: {sum(notifications2)} \n Average: {round(sum(notifications2) / len(notifications2))}")