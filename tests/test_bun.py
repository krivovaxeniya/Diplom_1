import allure
import pytest
from data import Data
from praktikum.bun import Bun


class TestBun:

    @allure.title('Проверка метода get_name() для Bun')
    @allure.description('Создаются объекты Bun с различными сочетаниями наименования и цены, выполняется проверка '
                        'того, что переданное наименование соответствует возвращаемому')
    @pytest.mark.parametrize('bun_name, price', Data.buns)
    def test_get_name(self, bun_name, price):
        bun = Bun(bun_name, price)
        assert bun.get_name() == bun_name

    @allure.title('Проверка метода get_price() для Bun')
    @allure.description('Создаются объекты Bun с различными сочетаниями наименования и цены, выполняется проверка '
                        'того, что переданная цена соответствует возвращаемой')
    @pytest.mark.parametrize('bun_name, price', Data.buns)
    def test_get_price(self, bun_name, price):
        bun = Bun(bun_name, price)
        assert bun.get_price() == price
