print("****************************")
print("Gasoline Branch\n\n")

# Import_Libraries_here
import sys
from time import sleep
import random

def gasLevelGuage():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Thank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

