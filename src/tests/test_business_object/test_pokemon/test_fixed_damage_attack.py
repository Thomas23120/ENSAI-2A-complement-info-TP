from business_object.pokemon.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.statistic import Statistic

class TestFixedDamageAttack:
    def test_fixed_damage_attack(self):
        boule = FixedDamageAttack(10, "boule", "renvoie une boule")
        Pokemon_A = AttackerPokemon(Statistic(attack=100, defense=50), level=1, name="pikachu", type_pk="elec")
        Pokemon_D = DefenderPokemon(Statistic(attack=90, defense=30), level=5, name="myu", type_pk="normal")
        res = boule.compute_damage(Pokemon_A, Pokemon_D)
        assert res == 10

if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

