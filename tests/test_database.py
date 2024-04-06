import allure
from praktikum.database import Database
from unittest.mock import Mock


class TestDatabase:

    @allure.title('Проверка метода available_buns() для Database')
    @allure.description('Выполняется проверка того, что available_buns() возвращает значения buns для Database')
    def test_available_buns(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        mock_buns = [mock_bun]
        database = Database()
        database.buns = []
        database.buns.append(mock_buns)
        assert database.available_buns() == database.buns

    @allure.title('Проверка метода available_ingredients() для Database')
    @allure.description('Выполняется проверка того, что available_ingredients() возвращает значения ingredients для Database')
    def test_available_ingredients(self):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 100
        mock_ingredients = [mock_ingredient]
        database = Database()
        database.ingredients = []
        database.ingredients.append(mock_ingredients)
        assert database.available_ingredients() == database.ingredients
