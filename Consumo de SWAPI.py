import requests

url = 'https://swapi.dev/api/planets/?search=arid'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f'Hay {len(data["results"])} planetas cuyo clima es árido.')
    for planet in data['results']:
        print(f'El planeta {planet["name"]} aparece en las siguientes películas: {", ".join(planet["films"])}')
else:
    print(f'Error al obtener la información de la API: {response.status_code}')

import requests

url = 'https://swapi.dev/api/films/3/'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    wookies = [character for character in data['characters'] if 'wookie' in character]
    print(f'Hay {len(wookies)} Wookies en la sexta película.')
else:
    print(f'Error al obtener la información de la API: {response.status_code}')

import requests

url = 'https://swapi.dev/api/starships/'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    largest_starship = max(data['results'], key=lambda x: int(x['length']))
    print(f'La aeronave más grande en toda la saga es {largest_starship["name"]}, con una longitud de {largest_starship["length"]} metros.')
else:
    print(f'Error al obtener la información de la API: {response.status_code}')
