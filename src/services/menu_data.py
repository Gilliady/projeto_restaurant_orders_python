from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: set(Dish) = set()
        with open(source_path, "r", encoding="utf-8") as file:
            lines = file.readlines()[1:]
            self.file_to_dishes(lines)

    def file_to_dishes(self, lines):
        dishes = {}
        for line in lines:
            dish_name, dish_price, ingredient_name, amount = line.split(
                ",")
            dishes.setdefault(dish_name, {})
            dishes[dish_name]["dish_price"] = float(dish_price)
            dishes[dish_name][Ingredient(ingredient_name)] = int(amount)
        for key in dishes.keys():
            dish = Dish(key, dishes[key]["dish_price"])
            for ingredient in dishes[key].keys():
                if ingredient != "dish_price":
                    dish.add_ingredient_dependency(
                        ingredient, dishes[key][ingredient]
                    )
                self.dishes.add(dish)

    def __len__(self) -> int:
        return len(self.dishes)
