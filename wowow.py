import requests
import json

def getEmoji(sobsob):
    response = requests.get(f"https://github.com/cheatsnake/emojihub/commit/ac8740a89a4bad46a9c40ef44f4be5b13f33bd37#diff-f52e6975c1fff64036e70914311e48390fdcd30e8cfb3f1ac0a41b1083462f3f{sobsob.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None

    data = response.json()
    return {
        "name": data["name"],
        "category": data["category"],
        "group": data["group"]
    }

emoji = getEmoji("china")
print(emoji)