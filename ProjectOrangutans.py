print("****************************")
print("Gasoline Branch\n\n")

# Import_Libraries_here
import sys
from time import sleep
import random

# function that lists Gas Stations and randomly choosing one, and returning its value
def gasLevelGuage():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Thank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# function will call the gasLevelGuage to determine gas level and then find a close gas station, if low.
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1 )
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)
