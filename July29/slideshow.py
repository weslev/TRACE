from IPython import display
import time
import requests
import random

# Creates random date
def GetDate():
    date = "201" + str(random.randint(0, 8))
    date = date + "-" + str(random.randint(10, 12))
    date = date + "-" + str(random.randint(10, 28))
    return date

# User key goes here
key = "DEMO_KEY"

# URL to the API
url = f"https://api.nasa.gov/planetary/apod?api_key={key}"

randDate = GetDate()

# Refreshes photo every 10 seconds
while True:
    randDate = GetDate()
    response = requests.get(url + "&date=" + randDate).json()['url']
    display.display(display.Image(response))
    time.sleep(10)
    display.clear_output()
