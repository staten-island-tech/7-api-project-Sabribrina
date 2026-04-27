import requests
import json

def getCreature(sobsob):
    response = requests.get(f"docs.api.jikan.moe/anime/{id}/full{sobsob.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None

    data = response.json()
    return {
        "titles": data["titles"],
        "category": data["category"],
        "group": data["group"]
    }

creature = getCreature("Pacific Spiny Dogfish")
print(creature)

"data": {
    "mal_id": 0,
    "url": "string",
    "images": { … },
    "trailer": { … },
    "approved": true,
    "titles": [ … ],
    "title": "string",
    "title_english": "string",
    "title_japanese": "string",
    "title_synonyms": [ … ],
    "type": "TV",
    "source": "string",
    "episodes": 0,
    "status": "Finished Airing",
    "airing": true,
    "aired": { … },
    "duration": "string",
    "rating": "G - All Ages",
    "score": 0.1,
    "scored_by": 0,
    "rank": 0,
    "popularity": 0,
    "members": 0,
    "favorites": 0,
    "synopsis": "string",
    "background": "string",
    "season": "summer",
    "year": 0,
    "broadcast": { … },
    "producers": [ … ],
    "licensors": [ … ],
    "studios": [ … ],
    "genres": [ … ],
    "explicit_genres": [ … ],
    "themes": [ … ],
    "demographics": [ … ],
    "relations": [ … ],
    "theme": { … },
    "external": [ … ],
    "streaming": [ … ]
  }
}

""" def divide(a,b):
    try:
        result = a/ b
    except ZeroDivisionError:
        print("Cannot divide by 0")
    else:
        print(a/b)

divide (10,0) """