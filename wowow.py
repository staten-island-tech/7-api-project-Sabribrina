import requests
import json

def getChara(sobsob):
    response = requests.get(f"https://api.disneyapi.dev/character{sobsob.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)

chara = getChara("")
print(chara)