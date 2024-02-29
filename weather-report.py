
import requests

# Define the API endpoint and parameters
url = "https://api.worldweatheronline.com/premium/v1/weather.ashx"
params = {
    "key": "c2518278d0da4956bcb80622242802",  # Replace with your actual API key
    "q": "Krabi,Thailand",
    "date": "2023-01-01",  # Start date (change for desired year)
    "enddate": "2023-12-31",  # End date (change for desired year)
    "format": "json",
    "tp": "daily"  # Change to "monthly" for monthly data
}

# Send the request and handle the response
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # Access monthly rainfall data (structure may vary depending on the API)
    for month in data["weather"]:
        rainfall_mm = month.get("totalprecipMM")  # Adjust key based on API response
        print(f"{month['date']}: {rainfall_mm} mm")
else:
    print("Error:", response.status_code, response.text)
