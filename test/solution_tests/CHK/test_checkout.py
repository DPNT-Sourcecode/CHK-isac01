from solutions.CHK import checkout_solution
import pytest


@pytest.fixture
def prices():
    return {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }

class TestCheckout():
    def test_single_item(self, prices):
        assert checkout_solution.checkout("1A") == prices["A"]

    def test_all_items(self, prices):
        checkout_string = ",".join(map(lambda x: f"1{x}", prices.keys()))
        checkout_price = sum(prices.values())
        assert checkout_solution.checkout(checkout_string) == checkout_price
