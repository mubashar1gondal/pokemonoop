import requests as r, pprint
from IPython.display import clear_output as co

class Pokemon:
    def __init__(self, pokemon_name):
            d = r.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}').json()
            self.name = d['name']
            self.weight = d['weight']
            self.abilities = [ability_dict['ability']['name'] for ability_dict in d['abilities']]
            self.types = [x['type']['name'] for x in d['types']]
            self.poke_dict = {
            'name': d['name'],
            'weight': d['weight'],
            'abilities': [ability_dict['ability']['name'] for ability_dict in d['abilities']],
            'types': [x['type']['name'] for x in d['types']]
    }
       
            
            
    
p1 = input("What pokemon do you want? ").lower()
p2 = Pokemon(p1)
p2.poke_dict
