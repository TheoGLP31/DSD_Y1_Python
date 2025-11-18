screenTimes = [120, 95, 140, 160, 80, 100, 200]

print("Day 3: " + str(screenTimes[2]))

total = 0

for i in range(len(screenTimes)):
    total += screenTimes[i]

print("Total: " + str(total))
screenTimes[-1] = 500

highest = max(screenTimes)
lowest = min(screenTimes)

print("Highest: " + str(highest))
print("Lowest: " + str(lowest))