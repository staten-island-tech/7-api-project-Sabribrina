""" import requests
import json

def getChara(sobsob):
    response = requests.get(f"https://api.disneyapi.dev/character/{sobsob.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)

chara = getChara("291") """

import requests
import json

my_list = []
def getChara(sobsob):
    response = requests.get(f"https://api.disneyapi.dev/character/{sobsob.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)

import json
ask = input("what info do u want?? (type id numb)")
chara = getChara(ask)
my_list.append(getChara(ask))
print(my_list)
askk = input("what specific data? ex: name...")
print(my_list.index(askk))