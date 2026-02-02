import matplotlib.pyplot as plt
import pandas as pd

def produceLine():
    print("--" * 30)

df = pd.read_csv("pixelvault game sales.csv")

print(df.head())
produceLine()
print(df.tail())
produceLine()
print(f"Number of Rows: {len(df)}")
print(f"Number of Columns: {len(df.columns)}")
produceLine()

print(df.columns)
print(df.dtypes)

produceLine()
print("Numerical Columns: sale_id, price, quantity, total_sale")
print("Categorical Columns: category")
produceLine()

nullCount = df.isnull().sum().sum()
print(f"Total Null Values: {nullCount}")

duplicateCount = df.duplicated().sum()
print(f"Total Duplicated Values: {duplicateCount}")

numOfIncorrectCalculations = (df["total_sale"] != df["price"] * df["quantity"]).any()
print(f"Incorrect Calculations: {numOfIncorrectCalculations}")

frequencyValues = df["game_title"].mode()
print(f"The most frequently appeared game title is: {frequencyValues.values[0]}.")

categorySales = df.groupby(["category"])["total_sale"].sum().sort_values(ascending=False)
print(f"The category with the highest sales is: {categorySales.index[0]}")

totalSales = df.sort_values(["total_sale"], ascending=False)
print(totalSales.head(1)["total_sale"].values)