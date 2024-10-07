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

@pytest.fixture
def offers():
    return {
        "A": (3, 130),
        "B": (2, 45),
    }

class TestCheckout():
    def test_single_item(self, prices):
        assert checkout_solution.checkout("1A") == prices["A"]

    def test_all_items(self, prices):
        checkout_string = ",".join(map(lambda x: f"1{x}", prices.keys()))
        checkout_price = sum(prices.values())
        assert checkout_solution.checkout(checkout_string) == checkout_price

    def test_offers(self, offers):
        assert checkout_solution.checkout("3A") == 130
        assert checkout_solution.checkout("2B") == 45


class TestDecodeSKUs():
    def test_single_item(self):
        assert checkout_solution.decode_string("A") == [("A", 1)]



