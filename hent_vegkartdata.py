import requests
import json
import pandas as pd

url = "https://nvdbapiles-v3.atlas.vegvesen.no/vegobjekter/915?segmentering=true&egenskap=(11278%3D19031)%20AND%20(11278%3D19031)%20AND%20(11276%3D19024%20OR%2011276%3D19025%20OR%2011276%3D19026)&kartutsnitt=-677309.17%2C6219847.976%2C2492617.17%2C8243724.024&inkluder=alle"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    # Convert the JSON data to a pandas DataFrame
    df = pd.json_normalize(data['objekter'])
    # Write the data to a CSV file in the specified path
    df.to_csv('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data.csv', index=False)
else:
    print("Request failed with status code:", response.status_code)
