from business_object.pokemon.abstract_attack import AbstractAttack

class FixedDamageAttack(AbstractAttack):
    def compute_damage(self, attacking_pokemon, defending_pokemon):
        return self._power