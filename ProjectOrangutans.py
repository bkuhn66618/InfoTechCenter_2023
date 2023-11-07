print("\n****************************************************\n")
print("Weather Branch \n")

#import libraries here
import sys
import time
import random

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
