from django.test import TestCase
from shop.utils import *


class CalculateMoneyDefTestCase(TestCase):
    def test_sum_price_count(self):
        result = sum_price_count(price=100, count=10)
        self.assertEqual(result, 1000)

    def test_sum_price_2_count(self):
        self.count = sum_price_count(price=500, count=1)
        result = self.count
        self.assertEqual(result, 500)

    def test_sum_price_count_with_discount(self):
        result = sum_price_count(price=200, count=15, discount=5)
        self.assertEqual(result, 2850)


class CalculateMoneyClassTestCase(TestCase, CalculateMoney):
    def test_sum_price_count_pass(self):
        result = self.sum_price_count(price=400, count=19)
        self.assertEqual(result, 7600)

    def test_sum_price_count_with_discount(self):
        result = self.sum_price_count(price=400, count=30, discount=10)
        self.assertEqual(result, 10800)

    def test_sum_price(self):
        list_prices = [294, 2000, 100]
        result = self.sum_price(prices=list_prices)
        self.assertEqual(result, 2394)

    def test_sum_price_with_discount(self):
        list_prices = [200, 640, 720]
        result = self.sum_price(prices=list_prices, discount=10)
        self.assertEqual(result, 1404)

    def test_sum_price_more_element(self):
        list_price = [140, 25, 678, 70, 180, 21]
        result = self.sum_price(prices=list_price)
        self.assertEqual(result, 1114)
