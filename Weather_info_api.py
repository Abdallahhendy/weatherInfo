from requests import get
from pprint import PrettyPrinter

BASE_URL = "http://api.weatherapi.com/v1"
API_KEY = "4e5397e74d3a43e594a162505242312"

prnt = PrettyPrinter()

country_name = input("Enter the name of your country: ")
endpoints =f"{BASE_URL}/current.json?key={API_KEY}&q={country_name}&aqi=yes"

response = get(endpoints).json()

if "error" not in response:
    # the location details
    region = response["location"]["region"]
    country = response["location"]["country"]
    local_time = response["location"]["localtime"]

    # More details
    temperature_c = response["current"]["temp_c"]
    temperature_f = response["current"]["temp_f"]
    feels_like_c = response["current"]["feelslike_c"]
    feels_like_f = response["current"]["feelslike_f"]
    humidity = response["current"]["humidity"]
    wind_speed_kph = response["current"]["wind_kph"]
    wind_direction = response["current"]["wind_dir"]
    visibility_km = response["current"]["vis_km"]
    condition = response["current"]["condition"]["text"]


    print("\n======================= WEATHER REPORT =======================")
    print(f"Location: {region}, {country}")
    print(f"Local Time: {local_time}")
    print(f"Condition: {condition}")
    print(f"Temperature: {temperature_c}°C ({temperature_f}°F)")
    print(f"Feels Like: {feels_like_c}°C ({feels_like_f}°F)")
    print(f"Humidity: {humidity}%")
    print(f"Wind: {wind_speed_kph} kph, Direction: {wind_direction}")
    print(f"Visibility: {visibility_km} km")
    print("=============================================================")
else:
    print("Error occurred while retrieving weather data.")
