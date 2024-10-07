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
    items = decode_string(skus)
    if items == -1:
        return -1

    total = 0
    for item, quantity in items:
        if offers.get(item) is not None and quantity % offers.get(item)[0] == 0:
            total += offers.get(item)[1] * (quantity / offers.get(item)[0])
        total += quantity * prices.get(item)

    return total


def decode_string(skus):
    """Decodes and validates string input, returning an array of 2-tuples containing the item and quantity"""
    # Assuming string format for this round since not specified
    decoded_items = []
    for sku in skus.split(","):
        item = sku[-1].upper()
        if prices.get(item) is None:
            return -1

        try:
            quantity = int(sku[:-1])
        except ValueError:
            return -1

        decoded_items.append((item, quantity))

    return decoded_items


