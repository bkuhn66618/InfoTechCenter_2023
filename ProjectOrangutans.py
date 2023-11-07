"""
Our Welcome Screen will start our program letting
drivers know that the Infotech Center 2023 is loading
"""

# Import_Libraries_Here
import sys
import time
from time import sleep
import random

timeToSleep = 2

print("\n\n Welcome - InfoTech Center 2023\n")
time.sleep(timeToSleep)

# add code to have the ellipses add a dot every .5 seconds
x = 0
ellipsis = 1
while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    sys.stdout.write(
        "\r" + message)  # /r prints a carriage return first, so, message is printed on top of previous line
    time.sleep(0.5)
    if ellipsis == 3:
        ellipsis = 0
    elif ellipsis <= 3:
        ellipsis += 1
    else:
        sys.stdout.write("\r error")
        sys.exit()
    if x == 20:
        print("\r InfoTech Center 2023 finished loading")
        time.sleep(1)
        print("\n Operating System Loaded - Face Scanned - Access Granted")
print("\n***********************************************************************************************************\n")
print("Checking Current gas levels\n")
sleep(1)

# function that lists Gas Stations and randomly choosing one, and returning its value
def gasLevelGuage():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function with a list of GasStations
def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Exxon", "Meijer", "Cosco", "Marathon", "BP", "Circle K", "Wesco"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby


# function will call the gasLevelGuage to determine gas level and then find a close gas station, if low.
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1 )
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = gasLevelGuage()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is low... checking Google Maps for closest gas station.")
        sleep(1.5)
        print("The closest gas station is,", listOfGasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("You only have a Quarter of a Tank, checking Google Maps for best mapping gas station")
        sleep(1.5)
        print("The closest on route gas station is,", listOfGasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank has half of a tank of gas, it is plenty, but be sure to keep watch")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is Three Quarters full!")
    elif gasLevelIndicator == "Full Tank":
        print("Your gas tank is full! You don't need to check it for a while")
    else:
        print("Error has occured, please wait for the system to restart")
        sys.exit()
gasLevelAlertq()
print("\n****************************************************\n")
print("Checking Weather Conditions \n")
#create a function randomly choosing the weather from a list
def upcomingWeather():
    weatherForecast = ["Rain", "Snow", "Cloudy", "Cold", "Thunderstorm", "Hail", "Intense Temp Warning", "Blizzard", "Foggy", "Light Rain", "Freezing Rain", "Sunny", "Icy"]
    actualWeather = random.choice(weatherForecast)
    return actualWeather

# Variable to call weather() once in our Vehicle Response System (VRS)
weatherAlert = upcomingWeather()

#VRS() function will allow my vehicle to respond based on weather conditions
def vehicleResponseSystem():
    if weatherAlert == "Rain":
        print("\n The National Weather Service has updated your alarm by 15 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only to allow you to drive 45 mph.")
    elif weatherAlert == "Thunderstorm":
        print("\n The National Weather Service has updated your alarm by 25 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only to allow you to drive 35 mph.")
    elif weatherAlert == "Freezing Rain":
        print("\n The National Weather Service has updated your alarm by 20 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only to allow you to drive 40 mph.")
    elif weatherAlert == "Snow":
        print("\n The National Weather Service has updated your alarm by 30 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only to allow you to drive 40 mph.")
    elif weatherAlert == "Blizzard":
        print("\n The National Weather Service has updated your alarm by 35 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only to allow you to drive 35 mph.")
    elif weatherAlert == "Icy":
        print("\n The National Weather Service has updated your alarm by 50 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only to allow you to drive 25 mph.")
    elif weatherAlert == "Hail":
        print("\n The National Weather Service has updated your alarm by 1 hour because of the forecast of", weatherAlert)
        print("While hail is going, either stay in the vehicle, or run to the nearest shelter")
    elif weatherAlert == "Foggy":
        print("\n The National Weather Service has update your alarm by 15 minutes because of the forecast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 55 mph")
    elif weatherAlert == "Cloudy":
        print("The alarm will not be changed because it's only", weatherAlert)
        print("Could turn into rain.")
    elif weatherAlert == "Cold":
        print("The alarm will not be changed because it's only", weatherAlert)
    elif weatherAlert == "Sunny":
        print("There is nothing wrong with this day, so the alarm will not be changed because its", weatherAlert)
    elif weatherAlert == "Light Rain":
        print("The alarm will not be changed because it's only a bit of", weatherAlert)
        print("Could Turn into heavier rain")
    elif weatherAlert == "Intense Temp Warning":
        temp = ["Winter", "Summer"]
        temperature =random.choice(temp)
        if temperature == "Summer":
            print("\n The National Weather Service has updated your alarm by 30 minutes because of the forecast of a hot",weatherAlert)
            print("Remember to drink plenty of water during this time, and turn on plenty of air conditioning")
        elif temperature == "Winter":
            print("\n The National Weather Service has updated your alarm by 55 minutes because the forecast of a cold ", weatherAlert)
            print("Vehicle Response System has been engaged only allowing you to drive 30 mph, and remember to layer up for the cold")
    else:
        print("There has been an error in the system. Turning off system")
        sys.exit()
vehicleResponseSystem()
app = 0
while app == 0:
    app = int(input("What would you like to activate? (1 for gas, 2 for weather, 3 to close)"))
    if app == 1:
        gasLevelAlert()
        app = 0
    elif app == 2:
        upcomingWeather()
        vehicleResponseSystem()
        app = 0
    elif app == 3:
        print("Shutting down system")
        sys.exit()
    elif app >= 3:
        print("command does not exist")
        app = 0
    else:
        ("error has occurred, restarting system")
        sys.exit()