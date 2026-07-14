"""
Weather Application - Weather data display application
Demonstrates API integration and data visualization
"""

import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt

class WeatherApp:
    """Weather Application"""

    def __init__(self, api_key=None):
        """Initialize weather app"""
        self.api_key = api_key or "your_api_key_here"
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self, city):
        """Get current weather data"""
        url = f"{self.base_url}/weather?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_forecast(self, city, days=7):
        """Get weather forecast"""
        url = f"{self.base_url}/forecast?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data['list'][:days]
        except (KeyError, requests.exceptions.RequestException) as e:
            return {"error": str(e)}

    def display_weather(self, city):
        """Display current weather"""
        weather = self.get_current_weather(city)
        if "error" in weather:
            print(f"Error: {weather['error']}")
            return

        print("\n" + "="*50)
        print(f"📍 {weather['name']}, {weather['sys']['country']}")
        print(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)
        print(f"🌡️  Temperature: {weather['main']['temp']:.1f}°C")
        print(f"💨 Wind: {weather['wind']['speed']} m/s")
        print(f"💧 Humidity: {weather['main']['humidity']}%")
        print(f"☁️  Clouds: {weather['clouds']['all']}%")
        print(f"👁️  Visibility: {weather['visibility']} m")
        print(f"☀️  Weather: {weather['weather'][0]['main']} - {weather['weather'][0]['description'].title()}")
        print("="*50 + "\n")

    def display_forecast(self, city):
        """Display 7-day forecast"""
        forecast = self.get_forecast(city, days=7)
        if "error" in forecast:
            print(f"Error: {forecast['error']}")
            return

        print("\n" + "="*60)
        print(f"📊 7-Day Weather Forecast for {city}")
        print("="*60)
        print(f"{'Date':<15} {'Weather':<15} {'Temp':<10} {'Humidity':<12} {'Wind':<10}")
        print("-"*60)

        for data in forecast:
            date = datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d')
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            weather = data['weather'][0]['main']

            print(f"{date:<15} {weather:<15} {temp:.1f}°C {humidity:>8}% {wind:>8.1f} m/s")

        print("="*60 + "\n")

    def visualize_temperature(self, city):
        """Visualize temperature forecast"""
        forecast = self.get_forecast(city, days=7)
        if "error" in forecast:
            print(f"Error: {forecast['error']}")
            return

        dates = []
        temps = []
        weather_types = []

        for data in forecast:
            date = datetime.fromtimestamp(data['dt']).strftime('%m-%d')
            dates.append(date)
            temps.append(data['main']['temp'])
            weather_types.append(data['weather'][0]['main'])

        # Create visualization
        plt.figure(figsize=(10, 6))
        plt.plot(dates, temps, marker='o', color='red', linewidth=2, markersize=8)
        plt.title(f"Temperature Forecast for {city}", fontsize=14, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Temperature (°C)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()

        # Save and show
        filename = f"{city.replace(' ', '_')}_temperature.png"
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()

        print(f"✅ Temperature chart saved to {filename}")
        return filename

    def compare_cities(self, cities):
        """Compare weather in multiple cities"""
        print("\n" + "="*60)
        print("🌍 Weather Comparison Across Cities")
        print("="*60)

        results = {}
        for city in cities:
            weather = self.get_current_weather(city)
            if "error" not in weather:
                results[city] = {
                    'temp': weather['main']['temp'],
                    'humidity': weather['main']['humidity'],
                    'wind': weather['wind']['speed'],
                    'condition': weather['weather'][0]['main']
                }

        # Display comparison
        print(f"\n{'City':<20} {'Temp':<10} {'Humidity':<12} {'Wind':<10} {'Condition':<15}")
        print("-"*60)
        for city, data in results.items():
            print(f"{city:<20} {data['temp']:.1f}°C {data['humidity']:>8}% {data['wind']:>8.1f} m/s {data['condition']:<15}")
        print("="*60 + "\n")

        return results


# Usage examples
if __name__ == "__main__":
    # Create weather app
    app = WeatherApp(api_key="demo_key")

    # Get current weather
    print("🌤️  Current Weather")
    print("-" * 40)
    app.display_weather("London")
    app.display_weather("New York")
    app.display_weather("Tokyo")

    # Get forecast
    print("\n📅 7-Day Forecast")
    print("-" * 40)
    app.display_forecast("London")

    # Visualize temperature
    print("\n📈 Temperature Visualization")
    print("-" * 40)
    app.visualize_temperature("London")

    # Compare cities
    print("\n🌍 City Comparison")
    print("-" * 40)
    app.compare_cities(["London", "New York", "Tokyo", "Sydney"])

    print("✨ Weather app completed successfully!")
