import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ESP/Task_4a_2/Core Employer Set Project - Task4A - Data - Summer 2022 1.csv')


def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) Return data for a specific property type')
    print('4) Return data for a specific size of property')
    return int(input(""))

def alldata():
    print(df)

def checkint(number):
    try:
        number = int(number)
        return number
    except:
        return ""

def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result

def property_type_check(prop_type):
    
    df1 = df[df["Property Type"] == prop_type]

    print(df1)

x = mainmenu()
while x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
    if x == 1:
        alldata()
    elif x == 2:
        while True:
            print()
            region = input("Please enter the name of the region you would like to check: ")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. Jan-20 ")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. Jan-20 ")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                region_check(region, startdate, enddate)
                                break
                        break
                break
            else:
                print("Region not found")
    elif x == 3:
        while True:
            print()
            propertytype = input("Please enter the name of the property type you would like to check: ")
            propertydf = df[df["Property Type"] == propertytype]
            if len(propertydf) == 0:
                print("Property Type is invalid.")
            else:
                property_type_check(propertytype)
    elif x == 4:
        while True:
            print()
            numofrooms = input("Please enter the number of rooms you would like to filter by: ")
            numofrooms = checkint(numofrooms)
            if numofrooms == "":
                print("Please enter a numerical value.")
            else:
                roomdf = df[df["Rooms"] == numofrooms]
                print(roomdf)
    elif x == 5:
        while True:
            years = []
            propertytypes = list(df["Property Type"].unique())

            for year in list(df.columns)[4:]:
                years.append(year)

            mean_df = df.groupby("Property Type")[years].mean().mean()
            print(mean_df)
            if len(mean_df) != 0:
                plt.bar(propertytypes, mean_df)
                plt.show()
    x = mainmenu()