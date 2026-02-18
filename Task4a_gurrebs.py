import pandas as pd
import matplotlib.pyplot as plt

BASE_PATH = "ESP/End_Point_Task4a/"

#Displays the main menu and collects choice of menu item

def check_int(number):
    try:
        number = int(number)
        return number
    except:
        return ""

def menu():
    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show total sales for a specific service")
        print("3. Show product with highest average sale")

        main_menu_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)

#Menu item selection from user and validates it
def get_product_choice():
    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item from the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date

def get_average_price(startdate, enddate):
    df1 = pd.read_csv(BASE_PATH + "Task4a_data (1).csv")
    items = df1["Menu Item"].unique()
    averages = {}
    highest_value = 0
    highest_item = ""
    for i in range(len(items)):
        df2 = df1.loc[df1['Menu Item'] == items[i]]
        df3 = df2.loc[:,startdate:enddate]
        df4 = round(df3.mean().mean(), 2)
        if float(df4) > highest_value:
            highest_value = float(df4)
            highest_item = items[i]
        averages[items[i]] = float(df4)

    return averages, highest_value, highest_item

#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv(BASE_PATH + "Task4a_data (1).csv")
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    return df3

def get_selected_service(service, startdate, enddate):
    df1 = pd.read_csv(BASE_PATH + "Task4a_data (1).csv")
    df2 = df1.loc[df1["Service"] == service]
    df3 = df2.loc[:,startdate:enddate]

    return df3

def get_service_choice():
    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item from the list:")
        print("Please enter the number of the service (1-2)")
        print("1.  Lunch")
        print("2.  Dinner")
        print("######################################################")

        item_choice = check_int(input("Please enter the number of your choice (1-2): "))

        if item_choice == "":
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if item_choice != 1 and item_choice != 2:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                if item_choice == 1:
                    flag = False
                    return "Lunch"
                else:
                    flag = False
                    return "Dinner"

main_menu = menu()
if main_menu == 1:
    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
 
    extracted_data = get_selected_item(item, start_date, end_date)
    
    print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
    extract_no_index = extracted_data.to_string(index=False)

    print(extract_no_index)
elif main_menu == 2:
    service = get_service_choice()
    start_date = get_start_date()
    end_date = get_end_date()

    extracted_data = get_selected_service(service, start_date, end_date)
    print("Here is the sales data for the {} service between dates {} and {}:".format(service, start_date, end_date))
    extract_no_index = extracted_data.to_string(index=False)

    print(extract_no_index)
    choice = input("Would you like to visualise this data (Y/N)? ")

    if choice.upper() == "Y":
        plt.bar(extracted_data.keys(), service)
        plt.title("Average Sales for {} | {} - {}".format(service, start_date, end_date))
        plt.xlabel("Menu Item")
        plt.xticks(rotation=45)
        plt.ylabel("Average Sales")
        plt.show()
elif main_menu == 3:
    start_date = get_start_date()
    end_date = get_end_date()

    averages, highestvalue, highestitem = get_average_price(start_date, end_date)
    print("The highest selling product is {} with an average of {} from {} to {}.".format(highestitem, highestvalue, start_date, end_date))
    choice = input("Would you like to visualise this data (Y/N)? ")

    if choice.upper() == "Y":
        plt.bar(averages.keys(), averages.values())
        plt.title("Average Sales for each Menu Item | {} - {}".format(start_date, end_date))
        plt.xlabel("Menu Item")
        plt.xticks(rotation=45)
        plt.ylabel("Average Sales")
        plt.show()
else:
    print('This part of the program is still under development')