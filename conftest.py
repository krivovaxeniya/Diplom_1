import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture()
def create_burger():
    burger = Burger()
    burger_bun = Bun("white bun", 200)
    burger_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
    burger_filling = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    burger.set_buns(burger_bun)
    burger.add_ingredient(burger_sauce)
    burger.add_ingredient(burger_filling)
    return burger
