import requests, json

# Response will be saved here
weather_data="weather_data.json"

# Request to `openweathermap` API
api_key = "6423af6e554f98cf1e6b8c6a7700986b"   #REPLACE_WITH_YOUR_API_KEY
location = "Dhaka"
url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

# url = f"https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&appid={api_key}"
# print(url)


# Response
response = requests.get(url)

# Get `Place` and `Temperature` from the Response
if response.status_code == 200:
    json_data = response.json()
    print(f"Place: {json_data['name']}, Temperature: {json_data['main']['temp']} celsius")
else:
    print(f"Request failed with status code {response.status_code}")

# Save the Response to a file
with open(weather_data,"w") as file:
       json.dump(json_data,file,indent=4)

# Output:
# Place: Dhaka, Temperature: 27.99 celsius