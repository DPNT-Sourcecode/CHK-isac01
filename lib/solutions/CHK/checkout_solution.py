from collections import defaultdict

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

offers = {
    "A": [(3, 130), (5, 200)],
    "B": [(2, 45)],
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
        if offers.get(item):
            offer_quantity, offer_price = offers.get(item)
            total += offer_price * (quantity // offer_quantity) + price * (quantity % offer_quantity)
        else:
            total += quantity * prices.get(item)

    return total

def get_best_price(item, quantity):
    price = prices.get(item)
    if offers.get(item) is None:
        return quantity * price

    price_matrix = [0] + [float("inf")] * quantity
    for i in range(1, quantity+1):
        price_matrix[i] = min(price_matrix[i], price_matrix[i-1] + price)
        for offer_quantity, offer_price in offers.get(item, []):
            if i >= offer_quantity:
                price_matrix[i] = min(price_matrix[i], price_matrix[i-offer_quantity] + offer_price)

    return price_matrix[-1]

def decode_string(skus):
    """Decodes and validates string input, returning an array of 2-tuples containing the item and quantity"""
    decoded_items = defaultdict(int)
    for char in skus:
        if not (char.isalpha() and char.isupper()):
            return -1

        if prices.get(char) is None:
            return -1

        decoded_items[char] += 1

    return list(decoded_items.items())



