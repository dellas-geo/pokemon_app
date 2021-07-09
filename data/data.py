import json
import requests

# This script is run once to populate the static folder with data

pokemon_info_list = []

# Fetch pokemon info
with requests.Session() as session:
    for i in range(1, 152):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        response = requests.get(url).json()

        pokemon_info = {
            "name": (response["name"]),
            "types": [type_dict["type"]["name"] for type_dict in response["types"]],
            "stats": [stats_dict for stats_dict in response["stats"]],
        }

        pokemon_info_list.append(pokemon_info)

    i = 1
    for dict in pokemon_info_list:
        dict["number"] = i
        i += 1
        dict["stats"] = {
            stat_dict["stat"]["name"]: stat_dict["base_stat"]
            for stat_dict in dict["stats"]
        }
        dict["name"] = dict["name"].capitalize()
        dict["types"] = [type.capitalize() for type in dict["types"]]

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(pokemon_info_list, f, ensure_ascii=False, indent=2)

# Fetch pokemon images
with requests.Session() as session:
    for i in range(1, 152):
        url = f"https://pokeres.bastionbot.org/images/pokemon/{i}.png"
        image_response = requests.get(url)

        with open(f"static/pokemon_images/pokemon#{i}.png", "wb") as file:
            file.write(image_response.content)