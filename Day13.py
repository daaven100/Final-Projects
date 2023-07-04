import requests
import json

def get_weather(city):
    api_key = "0a45e42df734865c4f4ee8de7934013e"
    base_url = "http://api.weatherstack.com/current"

    # Make a GET request to the OpenWeatherMap API
    response = requests.get(f"{base_url}?q={city}&appid={api_key}&units=metric")

    if response.status_code == 200:
        weather_data = response.json()

        # Extract relevant weather information
        main_weather = weather_data["weather"][0]["main"]
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        # Display the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Main Weather: {main_weather}")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Unable to fetch weather data.")

def main():
    city = input("Enter the city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
