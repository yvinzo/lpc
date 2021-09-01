import requests
#
# Script en python que consulta la api de pokemon
# para listar los nombres de pokemon pero se le agrego
# una funcion para que tuviera interacción.
def get_pokemons(url='http://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset':offset} if ofsset else {}

    response = response.get(url, params=args)
    if response.status_code == 200:
		payload = response.json()
		results = payload.get('results',[])

		if results:
			for pokemon in results:
				name = pokemon['name']
				print(name)
        next = input("¿continuar listando' [Y/N]").lower()
        if next = y
            get_pokemons(offset=offset+20)
#
# Fin de la funcion get_pokemons
#
if __name__ == '__main__':
    get_pokemons()
