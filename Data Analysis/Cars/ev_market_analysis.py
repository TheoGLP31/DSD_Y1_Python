import matplotlib.pyplot as plt
import pandas as pd

EV_Market_Data = pd.read_csv("Data Analysis/Cars/ev_market_2026.csv")

USD_TO_GBP = 0.74

# Used to print out the header
def ProduceHeader():
    print("#" * 39)
    print("### Electric Market 2026 - Analysis ###")
    print("#" * 39)

# Takes Number (str) and Change (Bool - auto set to False), attempts to change the Number into an integer, if it can be it will return the number, otherwise ""
def CheckInt(Number, Change=False):
    if Change == True:
        try:
            Number = int(Number)
            return Number
        except:
            return ""
    else:
        try:
            int(Number)
            return Number
        except:
            return ""

# Prompts the user to input a number from a list of available currencies and then returns Currency (str)
def GetCurrency():
    Flag = True
    AvailableCurrencies = ["GBP (£)", "USD ($)"]

    while Flag:
        for i in range(len(AvailableCurrencies)):
            print(f"### {i + 1}. {AvailableCurrencies[i]}")
        
        CurrencyChoice = CheckInt(input("### Please select a currency: "), True)

        if CurrencyChoice == "":
            print("### Please enter a number.")
            Flag = True
        else:
            if not CurrencyChoice > len(AvailableCurrencies) + 1:
                print(f"### Currency Chosen: {AvailableCurrencies[CurrencyChoice - 1]}")
                Flag = False
            else:
                print("### Please enter a valid number.")

    return AvailableCurrencies[CurrencyChoice - 1]

def ViewVarientPrice(Varient):
    VarientAveragePrice = round(EV_Market_Data[EV_Market_Data["variant"] == Varient]["price_usd"].mean(), 2)

    print(f"### Average Price for {Varient} is ${VarientAveragePrice}")

# Takes all of the Varients from the DataFrame and puts them into a list, finds the Average Price for each varient and displays them in a bar chart
def ViewAllVarientPrices():
    Varients = EV_Market_Data["variant"].unique().tolist()
    VarientPrices = {}

    for i in range(len(Varients)):
        AverageVarientPrice = float(EV_Market_Data[EV_Market_Data["variant"] == Varients[i]]["price_usd"].mean())
        VarientPrices[Varients[i]] = round(AverageVarientPrice, 2)

    plt.bar(VarientPrices.keys(), VarientPrices.values())
    plt.xlabel("Varient")
    plt.xticks(rotation=45)
    plt.ylabel("Average Price ($)")
    plt.show()

# Prompts the user to enter a brand from a list of brands from the DataFrame - prints formatted and returns Brand (str)
def GetBrand():
    ProduceHeader()
    Brands = EV_Market_Data["brand"].unique().tolist()

    Flag = True

    while Flag:
        for i in range(len(Brands)):
            print(f"### {i + 1}. {Brands[i]}")

        BrandChoice = CheckInt(input("### Enter your choice: "), True)

        if BrandChoice == "":
            Flag = True
        else:
            if not BrandChoice > len(Brands) + 1:
                return Brands[BrandChoice - 1]

# Prompts the user to enter a model from a list of models from the DataFrame - prints formatted and returns Brand (str) \\ RELYS ON GetBrand() FUNCTION //
def GetModel():
    Brand = GetBrand()
    BrandModels = EV_Market_Data[EV_Market_Data["brand"] == Brand]["model"].unique().tolist()

    Flag = True

    while Flag:
        for i in range(len(BrandModels)):
            print(f"### {i + 1}. {BrandModels[i]}")

        ModelChoice = CheckInt(input("### Please enter your choice: "), True)

        if ModelChoice == "":
            print("### Please enter a number")
            Flag = True
        elif ModelChoice > len(BrandModels) + 1:
            print("### Please enter a correct value.")
        else:
            Model = BrandModels[ModelChoice - 1]

            Flag = False
    
    print(f"### Selected Model: {Model}")
    return Model

# Prompts the user to enter a varient from a list of varients from the DataFrame - prints formatted and returns Varient (str)
def GetVarient():
    Varients = EV_Market_Data["variant"].unique().tolist()
    Flag = True
    
    while Flag:
        for i in range(len(Varients)):
            print(f"### {i + 1}. {Varients[i]}")
        
        VarientChoice = CheckInt(input("### Enter varient choice: "), True)

        if VarientChoice > len(Varients) + 1:
            print("### Please enter a valid number.")
            Flag = True
        else:
            VarientChoice = Varients[VarientChoice - 1]
            Flag = False

    return VarientChoice

# Takes Number (float) as a parameter - function used to check the length of the characters after the "." in a float to ensure it is not less than 2, if it is it will add a 0 to the end
def Add0To1dp(Number):
    Number = str(Number)

    if len(Number.split(".")[1]) == 1:
        Number += "0"
        return Number
    else:
        return Number

# Takes Number (str) as a parameter - function used to add commas to a number
def AddCommasToNumber(Number):
    Result = "{:,}".format(Number)

    return Result

# Takes Brand (str) and Currency (str) as parameters - finds the average price of models from the brand and prints it formatted
def AveragePricePerBrand(Brand, Currency):
    ProduceHeader()
    print(f"### Selected Brand: {Brand}")
    print(f"### Selected Currency: {Currency}")

    BrandData = EV_Market_Data[EV_Market_Data["brand"] == Brand]

    AveragePrice = round(BrandData["price_usd"].mean(), 2)

    if Currency == "GBP (£)":
        AveragePrice *= USD_TO_GBP
        AveragePrice = round(AveragePrice, 2)

    print(f"### Average Price for {Brand} in {Currency}: {"£" if Currency == "GBP (£)" else "$"}{AddCommasToNumber(AveragePrice)}")

# Takes Model (str) and Currency (str) as parameters - finds the average price of the model and rounds it to 2 d.p. - prints average price formatted
def AveragePricePerModel(Model, Currency):
    AveragePrice = round(EV_Market_Data[EV_Market_Data["model"] == Model]["price_usd"].mean(), 2)
    CurrencySign = "$"

    if Currency == "GBP (£)":
        AveragePrice *= USD_TO_GBP
        CurrencySign = "£"
    AveragePrice = Add0To1dp(round(AveragePrice, 2))

    print(f"### Average Price for {Model}: {CurrencySign}{AveragePrice}")

# Collects all available brands into a lists, outputs them and takes a user input then finds the average price of all an puts them into a bar chart
def AveragePriceEveryBrand():
    Brands = EV_Market_Data["brand"].unique().tolist()
    BrandAveragePricesDict = {}

    for i in range(len(Brands)):
        BrandDF = EV_Market_Data[EV_Market_Data["brand"] == Brands[i]]
        BrandAveragePrices = BrandDF["price_usd"].mean()

        BrandAveragePricesDict[Brands[i]] = round(BrandAveragePrices, 2)

    plt.bar(BrandAveragePricesDict.keys(), BrandAveragePricesDict.values())
    plt.xlabel("Brand Name")
    plt.xticks(rotation=45)
    plt.ylabel("Price ($)")
    plt.show()

# Collects all safety ratings in the DataFrame and sorts them descending - prints the first 5
def Top5SafestModel():
    Top5 = EV_Market_Data[EV_Market_Data["safety_rating"] >= 1].sort_values("safety_rating", ascending=False)[0:5]

    for i in range(len(Top5)):
        Model = Top5.iloc[i]["model"]
        Brand = Top5.iloc[i]["brand"]
        Rating = Top5.iloc[i]["safety_rating"]

        print(f"{i + 1}. {Brand} - {Model} | {Rating}")

# Collects all safety ratings in the DataFrame and sorts them ascending - prints the first 5
def Bottom5SafestModel():
    Bottom5 = EV_Market_Data[EV_Market_Data["safety_rating"] <= 5].sort_values("safety_rating", ascending=True)[0:5]

    for i in range(len(Bottom5)):
        Model = Bottom5.iloc[i]["model"]
        Brand = Bottom5.iloc[i]["brand"]
        Rating = Bottom5.iloc[i]["safety_rating"]

        print(f"{i + 1}. {Brand} - {Model} | {Rating}")

# Takes Model (str) parameter - finds the average rating of the model and prints it formatted
def AverageRatingPerModel(Model):
    AverageRating = float(round(EV_Market_Data[EV_Market_Data["model"] == Model]["customer_rating"].mean(), 1))

    FullStars = int(AverageRating)
    HalfStars = 1 if (AverageRating - FullStars) >= 0.5 else 0
    EmptyStars = 5 - FullStars - HalfStars

    WholeRating = ("★" * FullStars) + ("⯪" * HalfStars) + ("☆" * EmptyStars)

    print(f"Average Rating for {Model} is: {AverageRating} | {WholeRating} ")

# Prompts the user with the main panel, allows them to choose from a list of options, calls the corresponding functions
def Main():
    Flag = True

    while Flag:
        ProduceHeader()
        print("### 1. Average Price for Specific Brand")
        print("### 2. Average Price for All Brands [GRAPH]")
        print("### 3. Average Price for Specific Model")
        print("### 4. Compare Ratings for Specific Model")
        print("### 5. View Top 5 Safest Models")
        print("### 6. View Bottom 5 Safest Models")
        print("### 7. View Average Prices for Specific Varient")
        print("### 8. View Average Prices for All Varients [GRAPH]")
        OptionChoice = CheckInt(input("### Please enter your choice: "))

        if OptionChoice == "":
            print("### Please enter a number.")
            Flag = True
        elif OptionChoice == "1":
            Brand = GetBrand()
            Currency = GetCurrency()
            AveragePricePerBrand(Brand, Currency)
        elif OptionChoice == "2":
            AveragePriceEveryBrand()
        elif OptionChoice == "3":
            Model = GetModel()
            Currency = GetCurrency()
            AveragePricePerModel(Model, Currency)
        elif OptionChoice == "4":
            Model = GetModel()
            AverageRatingPerModel(Model)
        elif OptionChoice == "5":
            Top5SafestModel()
        elif OptionChoice == "6":
            Bottom5SafestModel()
        elif OptionChoice == "7":
            Varient = GetVarient()
            ViewVarientPrice(Varient)
        elif OptionChoice == "8":
            ViewAllVarientPrices()

Main()