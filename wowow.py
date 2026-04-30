import requests
import json

def getChara(sobsob):
    response = requests.get(f"https://api.disneyapi.dev/character/{sobsob.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return data

chara = getChara("291")

result = {}
for charas in chara:
    result.update(charas)

print(result)
print(result['name'])