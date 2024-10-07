from solutions.CHK import checkout_solution


class TestCheckout():
    def test_single_item(self):
        assert checkout_solution.checkout("1A") == 50


