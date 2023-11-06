import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Restriction, Ingredient


# Req 2
def test_dish():
    tomato = Ingredient("tomate")
    cheese = Ingredient("queijo mussarela")
    meat = Ingredient("carne")
    garlic = Ingredient("alho")
    pasta = Ingredient("massa de lasanha")
    lasagna = Dish("lasagna", 25.50)
    lasagna2 = Dish("lasagna", 25.50)
    lasagna.add_ingredient_dependency(tomato, 2)
    lasagna.add_ingredient_dependency(cheese, 5)
    lasagna.add_ingredient_dependency(meat, 1)
    lasagna.add_ingredient_dependency(pasta, 2)
    lasagna.add_ingredient_dependency(garlic, 1)
    lasagna2.add_ingredient_dependency(tomato, 2)
    lasagna2.add_ingredient_dependency(cheese, 5)
    lasagna2.add_ingredient_dependency(meat, 1)
    lasagna2.add_ingredient_dependency(pasta, 2)
    lasagna2.add_ingredient_dependency(garlic, 1)
    assert lasagna == lasagna2
    assert lasagna.recipe == {
        tomato: 2,
        cheese: 5,
        meat: 1,
        pasta: 2,
        garlic: 1,
    }
    assert lasagna.name == "lasagna"
    assert lasagna.price == 25.50
    assert repr(lasagna) == "Dish('lasagna', R$25.50)"
    assert hash(lasagna) == hash("Dish('lasagna', R$25.50)")
    assert lasagna.get_ingredients() == {
        tomato,
        cheese,
        meat,
        pasta,
        garlic,
    }
    assert lasagna.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        }
    with pytest.raises(TypeError):
        Dish("dish_invalid_price", "invalid_price")
    with pytest.raises(ValueError):
        Dish("dish_invalid_price", -25.50)
