import requests
import pprint

p1 = requests.get("https://pokeapi.co/api/v2/pokemon/lapras").json()
p2 = requests.get("https://pokeapi.co/api/v2/pokemon/charizard").json()
p3 = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()
p4 = requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur").json()
p5 = requests.get("https://pokeapi.co/api/v2/pokemon/ditto").json()
p6 = requests.get("https://pokeapi.co/api/v2/pokemon/jigglypuff").json()
p7 = requests.get("https://pokeapi.co/api/v2/pokemon/eevee").json()
p8 = requests.get("https://pokeapi.co/api/v2/pokemon/snorlax").json()
p9 = requests.get("https://pokeapi.co/api/v2/pokemon/mewtwo").json()
p10 = requests.get("https://pokeapi.co/api/v2/pokemon/mew").json()
p11 = requests.get("https://pokeapi.co/api/v2/pokemon/charmander").json()
p12 = requests.get("https://pokeapi.co/api/v2/pokemon/squirtle").json()
p13 = requests.get("https://pokeapi.co/api/v2/pokemon/gyarados").json()
p14 = requests.get("https://pokeapi.co/api/v2/pokemon/magikarp").json()
p15 = requests.get("https://pokeapi.co/api/v2/pokemon/gengar").json()
p16 = requests.get("https://pokeapi.co/api/v2/pokemon/dragonite").json()
p17 = requests.get("https://pokeapi.co/api/v2/pokemon/lugia").json()
p18 = requests.get("https://pokeapi.co/api/v2/pokemon/entei").json()
p19 = requests.get("https://pokeapi.co/api/v2/pokemon/jynx").json()
p20 = requests.get("https://pokeapi.co/api/v2/pokemon/slowpoke").json()

x = str(p1["abilities"])
y = str(p1["height"])
w = str(p1["weight"])
t = str(p1["types"])

print("Lapras has " + x + " abilities it's height is " +
      y + " it's weight is " + w + " and it's types are " + t)
