countryPop = {
    "Japan": 127000000, "Germany": 81000000, "Iran": 77000000,
    "UK": 64000000, "Canada": 33000000, "Australia": 23000000,
    "USA": 317000000, "Bulgaria": 7000000, "Sweden": 10000000
}

country1 = input("Choose the first country: ")
country2 = input("Choose the second coutry: ")

while country1 and country2 not in countryPop:
    country1 = input("Enter the name of the first country: ")
    country2 = input("Enter the name of the second country: ")
    print("Sorry can't find that information. Please try again")
print("I've found the information for you. The population of ", country1," and ",country2, " is: ",countryPop[country1] + countryPop[country2] , "\n")

