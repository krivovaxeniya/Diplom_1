import allure
import pytest
from data import Data
from praktikum.ingredient import Ingredient


class TestIngredient:

    @allure.title('Проверка метода get_price() для Ingredient')
    @allure.description('Создаются объекты Ingredient с различными сочетаниями типа, наименования и цены, выполняется '
                        'проверка того, что переданная цена соответствует возвращаемой')
    @pytest.mark.parametrize('ingredient_type, ingredient_name, price', Data.ingredients)
    def test_get_price(self, ingredient_type, ingredient_name, price):
        ingredient = Ingredient(ingredient_type, ingredient_name, price)
        assert ingredient.get_price() == price

    @allure.title('Проверка метода get_name() для Ingredient')
    @allure.description('Создаются объекты Ingredient с различными сочетаниями типа, наименования и цены, выполняется '
                        'проверка того, что переданное наименования соответствует возвращаемому')
    @pytest.mark.parametrize('ingredient_type, ingredient_name, price', Data.ingredients)
    def test_get_name(self, ingredient_type, ingredient_name, price):
        ingredient = Ingredient(ingredient_type, ingredient_name, price)
        assert ingredient.get_name() == ingredient_name

    @allure.title('Проверка метода get_type() для Ingredient')
    @allure.description('Создаются объекты Ingredient с различными сочетаниями типа, наименования и цены, выполняется '
                        'проверка того, что переданный тип соответствует возвращаемому')
    @pytest.mark.parametrize('ingredient_type, ingredient_name, price', Data.ingredients)
    def test_get_type(self, ingredient_type, ingredient_name, price):
        ingredient = Ingredient(ingredient_type, ingredient_name, price)
        assert ingredient.get_type() == ingredient_type
