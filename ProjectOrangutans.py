print("****************************")
print("Gasoline Branch\n\n")

# Import_Libraries_here
import sys
from time import sleep
import random

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

gasLevelAlert()