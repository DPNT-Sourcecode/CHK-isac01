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
        assert checkout_solution.checkout("A") == prices["A"]

    def test_all_items(self, prices):
        checkout_string = "".join(prices.keys())
        checkout_price = sum(prices.values())
        assert checkout_solution.checkout(checkout_string) == checkout_price

    def test_offers_basic(self, offers):
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BB") == 45

    def test_offers_advances(self):
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBB") == 75

    def test_invalid_item(self):
        assert checkout_solution.checkout("Z") == -1


class TestDecodeSKUs():
    def test_single_item(self):
        assert checkout_solution.decode_string("A") == [("A", 1)]

    def test_lowercase(self):
        assert checkout_solution.decode_string("a") == [("A", 1)]

    def test_multiple_items(self):
        assert checkout_solution.decode_string("AAA") == [("A", 3)]

    def test_invalid(self):
        assert checkout_solution.decode_string("-") == -1
        assert checkout_solution.decode_string("1") == -1
        assert checkout_solution.decode_string("abc1") == -1


