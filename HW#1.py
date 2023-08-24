import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
resp = requests.get(url)
most_int_hero = 0
most_int_hero_name = ''
for heroes in resp.json():
    if heroes["name"] == "Hulk" or heroes["name"] == "Captain America" or heroes["name"] == "Thanos":
        print(f' интеллект персонажа {heroes["name"]} равен {heroes["powerstats"]["intelligence"]}')
        if heroes["powerstats"]["intelligence"] > most_int_hero:
            most_int_hero_name = heroes["name"]
print(f' Самый высокий интеллект у персонажа {most_int_hero_name}')
