import allure
import pytest
from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:

    @allure.title('Проверка метода set_buns() для Burger')
    @allure.description('Выполняется проверка того, что наименование bun в Burger соответствует переданному')
    def test_set_buns(self):
        mock_bun = Mock()
        mock_bun.name = 'black bun'
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Проверка метода add_ingredient() для Burger')
    @allure.description('Добавляется ингредиент в Burger, выполняется проверка того, что добавленный ингредиент '
                        'присутствует в ingredients')
    def test_add_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.name = 'hot sauce'
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    @allure.title('Проверка метода remove_ingredient() для Burger')
    @allure.description('Добавляются два ингредиента в Burger, выполняется удаление одного из них. Выполняется '
                        'проверка того, что удаленный ингредиент отсутствует в ingredients')
    def test_remove_ingredient_from_ingredients(self):
        mock_bun = Mock()
        mock_bun.name = 'black bun'
        mock_sauce = Mock()
        mock_sauce.name = 'hot sauce'
        burger = Burger()
        burger.add_ingredient(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(1)
        assert mock_bun in burger.ingredients and mock_sauce not in burger.ingredients

    @allure.title('Проверка метода move_ingredient() для Burger')
    @allure.description('Добавляются два ингредиента в Burger, выполняется перемещение ингредиентов. Выполняется '
                        'проверка того, что ингредиенты соответствуют новым индексам')
    def test_move_ingredient(self):
        mock_bun = Mock()
        mock_bun.name = 'black bun'
        mock_sauce = Mock()
        mock_sauce.name = 'hot sauce'
        burger = Burger()
        burger.add_ingredient(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_sauce and burger.ingredients[1] == mock_bun

    @allure.title('Проверка метода get_price() для Burger при наличии в составе только bun')
    @allure.description('В бургер добавляется только bun. Выполняется проверка возвращаемой цены')
    def test_get_price_only_bun(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'black bun'
        mock_bun.get_price.return_value = 100
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.get_price() == mock_bun.get_price()*2

    @allure.title('Проверка метода get_price() для Burger при наличии в составе нескольких ингредиентов')
    @allure.description('В бургер добавляется два ингредиента - bun и sauce. Выполняется проверка возвращаемой цены')
    def test_get_price_bun_and_ingredient(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'black bun'
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 100
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == mock_bun.get_price()*2+mock_ingredient.get_price()

    @allure.title('Проверка метода get_receipt() для Burger при наличии в составе нескольких ингредиентов')
    @allure.description('Создается Burger. Выполняется проверка наличия всех ингредиентов и цены в рецепте')
    def test_get_receipt(self, create_burger):
        burger = create_burger
        price = burger.get_price()
        assert burger.get_receipt() == ('(==== white bun ====)\n'
                                        '= sauce sour cream =\n'
                                        '= filling cutlet =\n'
                                        '(==== white bun ====)\n'
                                        '\n'
                                        f'Price: {price}')
