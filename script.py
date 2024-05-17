import requests

# pikachu_data = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

# # print(pikachu_data)

# json_recuperer = pikachu_data.json()

# # print(json_recuperer)

# recuperer_nom = json_recuperer['name']

# print(recuperer_nom)

def combat (name1,name2) :
    pokemon_data1 = requests.get('https://pokeapi.co/api/v2/pokemon/'+ name1)
    json_recuperer1 = pokemon_data1.json()
    
    pokemon_data2 = requests.get('https://pokeapi.co/api/v2/pokemon/'+ name2)
    json_recuperer2 = pokemon_data2.json()
    if json_recuperer1['id'] < json_recuperer2['id'] :
        print(name1,'a un plus petit id')
        return {'id de'+ requests.get('https://pokeapi.co/api/v2/pokemon/'+ name1) :json_recuperer1['id'], 'id_name2':json_recuperer2['id'], 'winner':name2}

    else :
        print(name1,'a un plus grand id')
        return {'id de'+ requests.get('https://pokeapi.co/api/v2/pokemon/'+ name2) :json_recuperer1['id'], 'id_name2':json_recuperer2['id'], 'winner':name1}
    
print(combat('pikachu','charmeleon'))


