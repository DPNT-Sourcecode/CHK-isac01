from solutions.CHK import checkout_solution
import pytest


@pytest.fixture
def prices():
    return checkout_solution.prices

@pytest.fixture
def offers():
    return checkout_solution.offers

class TestCheckout():
    def test_single_item_A(self, prices):
        assert checkout_solution.checkout("A") == prices["A"]

    def test_single_item_F(self, prices):
        assert checkout_solution.checkout("F") == prices["F"]

    def test_all_items(self, prices):
        checkout_string = "".join(prices.keys())
        checkout_price = sum(prices.values())
        assert checkout_solution.checkout(checkout_string) == checkout_price

    def test_nonexistent_item(self):
        assert checkout_solution.checkout("Z") == -1

    def test_empty(self):
        assert checkout_solution.checkout("") == 0


class TestOffers():
    def test_offers_basic(self, offers):
        assert checkout_solution.checkout("A" * offers.get("A")[0]) == offers.get("A")[1]
        assert checkout_solution.checkout("B" * offers.get("B")[0]) == offers.get("B")[1]

    def test_offers_advanced(self):
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBB") == 75

    def test_multi_offers(self):
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAAA") == 400
        assert checkout_solution.checkout("AAAAAAAAAAAA") == 500
        assert checkout_solution.checkout("AAAAAAAAAAAAAAA") == 600

    def test_freebie_single(self, prices):
        assert checkout_solution.checkout("EEB") == prices.get("E") * 2

    def test_freebie_multiple(self, prices):
        assert checkout_solution.checkout("EEEEBB") == prices.get("E") * 4
        assert checkout_solution.checkout("EEEEEBB") == prices.get("E") * 5


class TestDecodeSKUs():
    def test_single_item(self):
        assert checkout_solution.decode_string("A") == {"A": 1}

    def test_lowercase(self):
        assert checkout_solution.decode_string("a") == -1

    def test_multiple_items(self):
        assert checkout_solution.decode_string("AAA") == {"A": 3}

    def test_invalid(self):
        assert checkout_solution.decode_string("-") == -1
        assert checkout_solution.decode_string("1") == -1
        assert checkout_solution.decode_string("abc1") == -1

