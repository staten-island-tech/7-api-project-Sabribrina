import requests
import json

def getChara(sobsob):
    response = requests.get(f"https://api.disneyapi.dev/character/{sobsob.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)

chara = getChara("291")

for key, value in chara.items():
    print(key, "→", value)

""" chara = {
    "name": "Aqua",
    "url": "https://static.wikia.nocookie.net/disney/images/0/0a/Aqua_KHIII.png",
}
print(chara["name"]) """