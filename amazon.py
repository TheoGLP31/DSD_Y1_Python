import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    return pd.read_csv("0902_work/amazon_sales_dataset.csv")

#########################
df = get_data()
#########################
print(df.head())

print(f"Number of Rows: {len(df)}")
print(f"Number of Columns: {len(df.columns)}")
#########################
total_revenue = round(df["total_revenue"].sum(), 2)
sales_value = round(df["price"].mean(), 2)
print(f"Total Sales: £{total_revenue}")
print(f"Average Sales: £{sales_value}")
#########################
grouped_by_category = df.groupby("product_category")
total_by_category = grouped_by_category["total_revenue"].sum()

plt.bar(df["product_category"].unique(), total_by_category)
plt.title("Total Sales by Category")
plt.xlabel("Product Category")
plt.xticks(rotation=45)
plt.ylabel("Total Sales")
plt.show()
#########################
grouped_by_region = df.groupby("customer_region")["total_revenue"].sum()

plt.bar(df["customer_region"].unique(), grouped_by_region.values)
plt.title("Sales by Region")
plt.xlabel("Regions")
plt.xticks(rotation=45)
plt.ylabel("Sales")
plt.show()