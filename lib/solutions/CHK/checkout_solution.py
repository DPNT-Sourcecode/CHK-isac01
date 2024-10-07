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

freebies = {
    # Example: Buy 3 of A, get 2 B for free would be
    # "A": (3, "B", 2)
    "E": (2, "B", 1)
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = decode_string(skus)
    if items == -1:
        return -1

    total = 0
    for item, quantity in items.items():
        total += get_best_price(item, quantity)

    return total

def decode_string(skus):
    """Decodes and validates string input, returning a dictionary mapping items to their quantities"""
    decoded_items = defaultdict(int)
    for char in skus:
        if not (char.isalpha() and char.isupper()):
            return -1

        if prices.get(char) is None:
            return -1

        decoded_items[char] += 1

    return decoded_items.items()

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

def apply_freebies(items):
    for item, quantity in items.items():
        if freebies.get(item) is None:
            continue

        times_applied = quantity // freebies.get(item)[0]
        freebie = freebies.get(item)[1]
        num_freebies = freebies.get(item)[2] * times_applied

        # Max to ensure doesn't go below 0
        items[freebie] = max(items[freebie] - num_freebies, 0)

