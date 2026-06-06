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
from tkinter import *

def getChara():
    try:
        ID = int(Enter.get())
    except ValueError:
        print("Put numbers in the text box")
        return "Type a number in the text box "
    
    response = requests.get(f"https://api.disneyapi.dev/character/{ID}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    else: 
        data = response.json()
        print(data)
        try:
            responsename.config(text = f"name = {data['data']['name']}")
            films.config(text = f"films = {data['data']['films']}")
            shortfilms.config(text = f"shortfilms = {data['data']['shortFilms']}")
            tvshows.config(text = f"tvshows = {data['data']['tvShows']}")
            allies.config(text = f"allies = {data['data']['allies']}")
            enemies.config(text = f"enemies = {data['data']['enemies']}")
            videogames.config(text = f"videogame = {data['data']['videoGames']}")
        except TypeError:
            responsename.config(text = "Invalid response please try another number")

window = Tk()
window.geometry("700x300") # set the size (width x height)

Title = Label(master = window, text = "yahoo game")
Title.pack()
Enter = Entry(master=window)
Enter.pack()

Instruct = Label(master = window, text = "What id u looking for? type a number")
Instruct.pack()

Ask = Label(master = window, text = "ask")
Ask.pack()

Buttonn = Button(master = window, text = "find", command = getChara)
Buttonn.pack()

responsename = Label(window, text = "")
responsename.pack()
films = Label(window, text = "")
films.pack()
shortfilms = Label(window, text = "")
shortfilms.pack()
tvshows = Label(window, text = "")
tvshows.pack()
allies = Label(window, text = "")
allies.pack()
enemies = Label(window, text = "")
enemies.pack()
videogames = Label(window, text = "")
videogames.pack()

window.mainloop()