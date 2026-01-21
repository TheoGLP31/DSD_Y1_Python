import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

issues = pd.read_csv("Task4a_data.csv")

# Checks if the entered value is between a set of numbers (1 and 10)
# Takes Value, Min, and Max
# Returns True if between, False if not
def check_between(value, min, max):
    if value >= min and value <= max:
        return True
    else:
        return False

# Gets the average number of days taken to resolve issues
# Takes no inputs
# Returns average days (FLOAT/REAL)
def average_days_to_resolve():
    days_to_resolve = issues["Days To Resolve"]
    total_days = 0
    length_of_issues = len(issues)
    for i in range(len(days_to_resolve)):
        total_days += days_to_resolve.values[i]
    average_days = total_days / length_of_issues

    return average_days

# Filters the issues by regions
# Takes no inputs
# Returns filtered dataset (DataFrame)
def filter_by_region():
    flag = True
    available_regions = []
    for i in range(len(issues)):
        current_region = issues.loc[i]["Region"]
        if current_region in available_regions:
            pass
        else:
            available_regions.append(current_region)
    while flag:
        print("####################################################")
        print("################# Filter by Region #################")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        highest_choice = 1
        for i in range(len(available_regions)):
            print(f"### {available_regions[i]}")
            highest_choice += 1
        selected_region = input("Enter Region to Filter By: ")
        if selected_region in available_regions:
            new_df = issues[issues["Region"] == selected_region]
            flag = False
        else:
            print("Sorry, you did not enter a valid option. You must enter the full name of the Region.")
            flag = True

    return new_df

def get_data_visual_type():
    types = ["Average Number of Days to Resolve Issue", "Total Number of Issues Comparison"]
    visualisation_type = input(f"Choose from the following: {types}")

    print(visualisation_type)

# Outputs the initial menu and validates the input
def main_menu(number_of_inputs):
    flag = True

    while flag:
        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Average days to resolve issues")
        print("### 3. Filter by region")

        choice = input('Enter your number selection here: ')

        try:
            choice = int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            if choice > number_of_inputs:
                print(f"Sorry, you did not enter a valid option. You must enter a number between 1 and {number_of_inputs}")
                flag = True
            else:
                print('Choice accepted!')
                choice = str(choice)
                flag = False

    return choice

# Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:
        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            choice = int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            choice_between = check_between(choice, 1, 4)
            if choice_between == True:
                print('Choice accepted!')
                choice = int(choice)
                flag = False
            else:
                print("Sorry, you did not enter a valid option. Your choice must be between 1 and 4")
                flag = True

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    
    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    issues = pd.read_csv("Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg

number_of_inputs = 4

main_menu_choice = main_menu(number_of_inputs)
if main_menu_choice ==  "1":
    total_menu_choice = total_menu()
    print(get_total_data(total_menu_choice))
if main_menu_choice == "2":
    print(f"The average number of days to resolve an issue is {average_days_to_resolve()}")
if main_menu_choice == "3":
    filtered_df = filter_by_region()
    print(filtered_df)
if main_menu_choice == "4":
    get_data_visual_type()