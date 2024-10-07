from collections import defaultdict

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
        price = prices.get(item)
        if offers.get(item) and quantity % offers.get(item)[0] == 0:
            offer_quantity, offer_price = offers.get(item)
            total += offer_price * (quantity // offer_quantity) + price * (quantity % offer_quantity)
        else:
            total += quantity * prices.get(item)

    return total


def decode_string(skus):
    """Decodes and validates string input, returning an array of 2-tuples containing the item and quantity"""
    if skus == "":
        return -1

    decoded_items = defaultdict(int)
    for char in skus:
        if not char.isalpha():
            return -1

        decoded_items[char.upper()] += 1

    return list(decoded_items.items())







