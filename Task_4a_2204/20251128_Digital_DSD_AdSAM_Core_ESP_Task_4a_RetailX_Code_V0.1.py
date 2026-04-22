import pandas as pd
import matplotlib.pyplot as plt

RetailX_data = pd.read_csv("ESP/Task_4a_2204/Task4a_RetailX_data.csv")

#Outputs the main menu and checks the user input
def main_menu():
    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Total sales by product")
        print("2. Total sales by category")
        print("3. Total profits by category")
        print("4. Total income by category")
        print("5. Visualisation Menu")

        choice = input('Enter your number selection here: ')

        if choice.isdigit():
            flag = False
        else:
            flag = True

    return int(choice)

#Generates submenu of available product codes and allows user to select a product to view
def get_product_id():
    df = RetailX_data

    product_codes = df["Product ID"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product code:")
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        
        product_ID = product_codes[selection -1]
   
    print("You have selected product id:",product_ID)
    return product_ID

#Generates submenu of available categories to select a category to view
def get_category():
    df = RetailX_data

    categories = df["Category"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a category:")
        for i in range(len(categories)):
            print(i+1, " ", categories[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        
        chosen_cateogry = categories[selection -1]
   
    print("You have selected: ", chosen_cateogry)
    return chosen_cateogry 

#gets and converts user input from string to date format
def get_date(start_end):
    
    flag = True
    
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        try:
           pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return date

#extracts data based on product ID within a user specified date range.
def get_data_by_ID_and_date(product_id, start_date, end_date):
    all_data = RetailX_data
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date,format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]

    return extracted_data

#extracts data based on category within a user specified date range.
def get_data_by_category_and_date(category, start_date, end_date):
    all_data = RetailX_data
    product_data = all_data.loc[all_data["Category"] == category].copy()

    product_data["Date"] = pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    date_range = (product_data["Date"] >= pd.to_datetime(start_date,format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]

    return extracted_data

def get_profits_by_category_and_date(category, start_date, end_date):
    category_df = get_data_by_category_and_date(category, start_date, end_date)
    sales_list = category_df["Sales Price"].to_list()
    cost_list = category_df["Cost Price"].to_list()

    total_profits = 0

    for i in range(len(sales_list)):
        total_profits += (sales_list[i] - cost_list[i])
    
    total_profits = round(total_profits, 2)
    total_profits_split = str(total_profits).split(".")

    if len(total_profits_split[1]) == 1:
        total_profits_split[1] += "0"
    
    new_total_profits_str = ""
    for i in range(len(total_profits_split)):
        new_total_profits_str = total_profits_split[0] + "." + total_profits_split[1]

    return new_total_profits_str

def get_income_by_category_and_date(category, start_date, end_date):
    category_df = get_data_by_category_and_date(category, start_date, end_date)
    sales_list = category_df["Sales Price"].to_list()

    total_profits = 0

    for i in range(len(sales_list)):
        total_profits += (sales_list[i])
    
    total_profits = round(total_profits, 2)
    total_profits_split = str(total_profits).split(".")

    if len(total_profits_split[1]) == 1:
        total_profits_split[1] += "0"
    
    new_total_profits_str = ""
    for i in range(len(total_profits_split)):
        new_total_profits_str = total_profits_split[0] + "." + total_profits_split[1]

    return new_total_profits_str

#generates a total of the number of items sold for the extracted data
def calculate_total_sale(date_ID, product_id, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for product {}, between {} and {} was: {}'.format(product_id, start_date, end_date, total_sales))
    
#generates a total of the number of items sold for the extracted data
def calculate_total_sale_category(date_ID, category, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for category {}, between {} and {} was: {}'.format(category, start_date, end_date, total_sales))

def check_int(number, change=False):
    if change == True:
        try:
            number = int(number)
            return number
        except:
            return ""
    else:
        try:
            int(number)
            return number
        except:
            return ""
        
def graph_menu(choice1, choice2="", choice3=""):
    flag = True
    graph_choice = ""

    while flag:
        print("-"*66)
        print("---------- RetailX Sales Visualisation Module ------------- ")
        print("-"*66)
        print("")
        print("------------------------ Graph Menu ----------------------- ")
        print(f"1. {choice1}")
        if choice2:
            print(f"2. {choice2}")
        if choice3:
            print(f"3. {choice3}")

        graph_choice = check_int(input("Enter graph choice or 'n' to exit this menu: "), False)
        if graph_choice.lower() == "n":
            return ""
        elif graph_choice == "":
            print("Please enter a valid choice.")
            flag = True
        elif graph_choice == "1":
            flag = False
        elif graph_choice == "2" and choice2:
            flag = False
        elif graph_choice == "3" and choice3:
            flag = False
        else:
            print("Please enter a valid choice.")

    if graph_choice == "1":
        print("")
    return graph_choice

main_menu_choice = main_menu()

if main_menu_choice == 1:
    product_id = get_product_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    calculate_total_sale (date_ID, product_id, start_date, end_date)
elif main_menu_choice == 2:
    category = get_category()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_category_and_date(category, start_date, end_date)
    calculate_total_sale_category(date_ID, category, start_date, end_date)
elif main_menu_choice == 3:
    category = get_category()
    start_date = get_date("start")
    end_date = get_date("end")
    total_profits = get_profits_by_category_and_date(category, start_date, end_date)
    print(f"Total Profits for {category}: £{total_profits}")
elif main_menu_choice == 4:
    category = get_category()
    start_date = get_date("start")
    end_date = get_date("end")
    total_income = get_income_by_category_and_date(category, start_date, end_date)
    print(f"Total Income for {category}: £{total_income}")
elif main_menu_choice == 5:
    graph_choices = [
        "View Total Sales of Products",
        "View Total Profits from Products",
        "View Total Sales per Category",
        "View Total Profits per Category"
    ]
    graph_menu(graph_choices[1], graph_choices[3], graph_choices[2])