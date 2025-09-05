from business_object.pokemon.abstract_attack import AbstractAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon
from abc import abstractmethod

class AbstractFormulaAttack(AbstractAttack):
    @abstractmethod
    def get_attack_stat(attacking_pokemon: AbstractPokemon)->float:
        pass

    @abstractmethod
    def get_defense_stat(defending_pokemon: AbstractPokemon)->float:
        pass

    def compute_damage(self, attacking_pokemon: AbstractPokemon, defending_pokemon: AbstractPokemon):
        return self._power
