import requests
import os
from dotenv import load_dotenv

def get_weather_data():
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the weather API key from the environment
    api_key = os.environ.get("weather_api")

    # City for which you want the weather
    city = "Cairns"

    # Construct the URL for the API request
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"