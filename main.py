# import
import requests, json
from twilio.rest import Client
import time
# URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# city
CITY = "CITY"
#API
API_KEY = "APIKEY"
# building URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
#Client api. for message bot
client = Client("DATA", "DATA")
# Read URL
response = requests.get(URL)
# Check for valid response from URL
if response.status_code == 200:
   # defining data(from URL)
   data = response.json()
   #finding wind
   main = data['wind']
   #finding wind degree
   wind = main['deg']
   #finding speed
   speed = main['speed']
   #displaying wind direction
   print(f"Wind degree: {wind}")
degree = True
while True:
  time.sleep(5)
  olddegree = degree
  degree = wind in range(45, 70)
 # sending message if wind is in direction
  if degree == olddegree:
   #client.messages.create(to="YOUR NUMBER", from_="BOT NUMBER",body="Alert, incoming wind")
   print ("printing from if")
   print (f"Degree: {degree}")
   print (f"Olddegree: {olddegree}")
   # no wind coming in direction
  else:
   client.messages.create(to="Your number", from_="bot number", body=f"warning incoming wind, coming at speeds of {speed} mph, and at the angle of {wind}. This might be a start up message ")
   print ("printing from else")
   print (f"Degree: {degree}")
   print (f"Olddegree: {olddegree}")

