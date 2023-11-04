from src.models.ingredient import Ingredient, Restriction# noqa: F401, E261, E501


# Req 1
def test_ingredient():
    mandioca = Ingredient("mandioca")
    queijo_mussarela = Ingredient("queijo mussarela")
    mandioca2 = Ingredient("mandioca")
    assert mandioca == mandioca2
    assert mandioca != queijo_mussarela
    assert mandioca.name == "mandioca"
    assert queijo_mussarela.name == "queijo mussarela"
    assert hash(mandioca) == hash(mandioca2)
    assert hash(mandioca) != hash(queijo_mussarela)
    assert repr(mandioca) == "Ingredient('mandioca')"
    assert repr(queijo_mussarela) == "Ingredient('queijo mussarela')"
    assert mandioca.restrictions == set()
    assert queijo_mussarela.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
        }
