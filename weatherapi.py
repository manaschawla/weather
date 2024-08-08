import requests
import pandas as pd
#enter your api key
api_key = '23ea82dd0423ef1ef85ba0213ab4dc30'
city_name = input("enter the name of the city: ")
#construct the api url
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&id=524901&appid={api_key}"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(response)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df)
