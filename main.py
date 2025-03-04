import requests
import json

API_KEY = "0ed4562233864263a00190058250403"  # Replace with your actual API key


def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    try:
        # Sending request to the API
        r = requests.get(url)
        r.raise_for_status()  # Raises an HTTP error if response code is not 200

        # Parsing JSON response
        wdic = json.loads(r.text)

        # Check if API returned an error
        if "error" in wdic:
            print(f"Error: {wdic['error']['message']}")
            return

        # Extract and print weather details
        temp_c = wdic['current']['temp_c']
        condition = wdic['current']['condition']['text']
        print(f"Temperature in {city}: {temp_c}°C")
        print(f"Weather Condition: {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")


# User input
city = input("Enter the name of the city: ").strip()
get_weather(city)
