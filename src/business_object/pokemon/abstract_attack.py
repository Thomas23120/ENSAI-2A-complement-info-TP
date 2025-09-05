from business_object.pokemon.abstract_pokemon import AbstractPokemon
from abc import ABC

class AbstractAttack(ABC):
    def __init__(self, power, name, description):
        self._power: int = power
        self._name: str = name
        self._description: str = description
    
    def compute_damage(
        self, attacking_pokemon: AbstractPokemon, defending_pokemon: AbstractPokemon
        ):
        pass