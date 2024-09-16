""" this code is to access weather of different cities"""
import requests
#enter your api key
api_key = "your api_key"
city_name = input("enter the name of the city: ")
#construct the api url
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&id=524901&appid={api_key}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    main = data['main']
    weather = data['weather'][0]
    temprature = main['temp']
    humidity = main['humidity']
    description = weather['description']
    print(f"""{city_name} city has temprature - {temprature}
         humidity - {humidity}
        weather description - {description.capitalize()}""")
else:
    print("city not found")
