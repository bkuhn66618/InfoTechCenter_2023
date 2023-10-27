"""
Our Welcome Screen will start our program letting
drivers know that the Infotech Center 2023 is loading
"""

# Import_Libraries_Here
import sys
import time

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
        print("InfoTech Center 2023 finished loading")
        time.sleep(1)
        print("\n Operating System Loaded - Face Scanned - Access Granted")