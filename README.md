Weather App

Description

This is a simple command-line Weather App that fetches real-time weather information for a given city using the WeatherAPI. The app makes HTTP requests to retrieve weather data in JSON format and extracts relevant details such as the current temperature in Celsius.

Features

Fetches real-time weather data for any city.

Displays current temperature in Celsius.

Uses WeatherAPI for accurate weather information.

Requirements

Python 3.x

requests library

Installation

Clone this repository:

git clone https://github.com/AryanRajputx1/Weather_App.git

Navigate to the project directory:

cd Weather_App

Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

Install the required dependencies:

pip install requests

Usage

Run the script:

python main.py

Enter the name of the city when prompted.

The app will fetch and display the current temperature.
