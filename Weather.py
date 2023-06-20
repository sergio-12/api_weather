import requests
API_KEY = "460b3e30218476101e9fb285bf03cbb8"
BASE_URL = " https://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name: ")
request_url = F"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] -273.15, 2)
    
    print("weather:" , weather)
    print("temperature:", temperature, "celsius" )
    
else:
    print("An error ocurred")

