import requests
import json


url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
response = requests.get(url)
print(response)

restaurant_data = {}

if response.status_code == 200:
    json_data = response.json()

    for item in json_data:
        restaurant_name = item["Company"]

        if restaurant_name not in restaurant_data:
            restaurant_data[restaurant_name] = []

        restaurant_data[restaurant_name].append({
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"]
        })

else:
    print(f"The error was {response.status_code}")


for restaurant_name, data in restaurant_data.items():
    file_name = f"{restaurant_name}.json"

    with open(file_name, "w") as restaurant_file:
        json.dump(data, restaurant_file, indent=4)
