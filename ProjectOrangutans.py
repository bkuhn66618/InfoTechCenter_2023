print("\n****************************************************\n")
print("Weather Branch \n")

#import libraries here
import sys
import time
import random

#create a function randomly choosing the weather from a list
def upcomingWeather():
    weatherForecast = ["Rain", "Snow", "Cloudy", "Cold", "Thunderstorm", "Hail", "Heat Stroke Warning", "Blizzard", "Foggy", "Light Rain", "Freezing Rain", "Sunny"]
    actualWeather = random.choice(weatherForecast)
    #return actualWeather
    print(actualWeather)

upcomingWeather()
