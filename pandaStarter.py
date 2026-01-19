import pandas as pd
import matplotlib.pyplot as plt

def produceLine():
    print("-" * 30)

"""
data = {
    "Name": ["Alex", "Jamie", "Sam"],
    "Attendance": [92, 85, 78],
    "Grade": ["B", "C", "D"]
}

df = pd.DataFrame(data)
df.loc[len(df)] = ["Theo", 69, "A"]
print(df)

produceLine()

print(df["Attendance"])

produceLine()

print(df["Attendance"].mean())

produceLine()
"""

df = pd.read_csv("students.csv", index_col=0)
print("df.head():")
print(df.head())

produceLine()

print("df.info():")
print(df.info())

produceLine()
"""
newDf = df[df["Attendance"] >= 85]
print(newDf)
"""

print(f"Number of learners in the dataset: {len(df)}")
print(f"Average Attendance {sum(df["Attendance"]) / len(df)}")
print(f"Highest Attendance: {df["Attendance"].max()}")
print(f"Lowest Attendance: {df["Attendance"].min()}")
below80Attendance = df[df["Attendance"] < 80]
atOrAbove90Attendance = df[df["Attendance"] >= 90]
print(f"Number of learners below 80% attendance: {len(below80Attendance)}")
print(f"Number of learners at or above 90% attendance: {len(atOrAbove90Attendance)}")

aAchievers = df[df["Grade"] == "A"]
bAchievers = df[df["Grade"] == "B"]
cAchievers = df[df["Grade"] == "C"]
dAchievers = df[df["Grade"] == "D"]
eAchievers = df[df["Grade"] == "E"]
fAchievers = df[df["Grade"] == "F"]

for i in range(0, 6):
    print(f"Number of people who achieved an {"A" if i == 0 else "B" if i == 1 else "C" if i == 2 else "D" if i == 3 else "E" if i == 4 else "F"}: {len(aAchievers) if i == 0 else len(bAchievers) if i == 1 else len(cAchievers) if i == 2 else len(dAchievers) if i == 3 else len(eAchievers) if i == 4 else len(fAchievers)}")

at_risk = df["Attendance"] < 80

df["AtRisk"] = False
df.loc[df["Attendance"] < 80, "AtRisk"] = True

print(df)

print(df.sort_values("Attendance", ascending=False))

temp_highest = 0

print(df.head())

percentages = percentages = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

plt.subplot(1, 2, 1)
plt.hist(df["Attendance"], bins=percentages)
plt.title("Attendance Distribution")
plt.xlabel("Percentage")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.bar(["A", "B", "C", "D", "E", "F"], [len(aAchievers), len(bAchievers), len(cAchievers), len(dAchievers), len(eAchievers), len(fAchievers)])
plt.xlabel("Grades")
plt.ylabel("Number of Achievers")
plt.title("Grade Breakdown")

plt.subplot(2, 1, 1)
plt.bar(df["Name"], df["Attendance"])
plt.xticks(rotation=45, ha="right")
plt.subplots_adjust(bottom=0.19)
plt.show()