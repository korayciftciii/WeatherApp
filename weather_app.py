import requests


def weather(city):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Get temperature in Celsius
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        location = data['name']
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']

        print(f"Location: {location}")
        print(f"Weather: {weather_desc}")
        print(f"Temperature: {temperature}°C")
    else:
        print("Failed to retrieve weather data.")


print("Enter the city name:")
city = input()
weather(city)
