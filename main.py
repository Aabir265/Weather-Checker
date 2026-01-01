import requests
from config import API_KEY
def get_weather(city):
    parms = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parms)
    if response.status_code != 200:
        print("Error fetching data from the weather API.")
        return None
    return response.json()
def display_weather(data):
    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print(f"\nWeather in {city}")
    print(f"🌡 Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌥 Condition: {condition}")
if __name__ == "__main__":
    city = input("Enter city name:")
    weather_data = get_weather(city)
    if weather_data:
        display_weather(weather_data)