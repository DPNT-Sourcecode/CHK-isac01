prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

offers = {
    "A": (3, 130),
    "B": (2, 45),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Assuming string format for this round since not specified
    for sku in skus.split(","):
        item = sku[-1].upper()
        if prices.get(item) is None:
            return -1

        try:
            quantity = int(sku[:-1])
        except ValueError:
            return -1



