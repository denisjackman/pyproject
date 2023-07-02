'''
    example of the pokemon api from https://pokeapi.co/
'''
import pokebase as pb
charmander = pb.pokemon('charmander')

print(f"charmander: {charmander}")
print(f"charmander.name: {charmander.name}")
print(f"charmander.id: {charmander.id}")
print(f"charmander.height: {charmander.height}")
print(f"charmander.weight: {charmander.weight}")
print(f"charmander.base_experience: {charmander.base_experience}")
print(f"charmander.order: {charmander.order}")
