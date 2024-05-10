import requests
import time

def get_highways_in_city():
    overpass_url = "https://overpass-api.de/api/interpreter"
    query = """
    [out:json];
    way["highway"](40.4957,-74.2571,40.9153,-73.6995);
    out;
    """
    try:
        response = requests.post(overpass_url, data=query)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if data["elements"]:
            highways = [element["tags"]["name"] for element in data["elements"] if "name" in element["tags"]]
            return highways
        else:
            print("No highways found in the city")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

# Example of using the function
highways = get_highways_in_city()
if highways:
    print("Highways in New York City:")
    for highway in highways:
        print(highway)

# To ensure compliance with the usage policy, add a delay between requests
time.sleep(1)
