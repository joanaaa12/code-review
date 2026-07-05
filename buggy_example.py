"""Small utility module with several intentionally planted bugs, used to test code review."""


def average(numbers):
    total = 0
    for i in range(len(numbers) + 1):  # BUG: off-by-one, will IndexError
        total += numbers[i]
    return total / len(numbers)


def get_discounted_price(price, discount_percent=10, cache={}):  # BUG: mutable default argument
    if price in cache:
        return cache[price]
    result = price - (price * discount_percent / 100)
    cache[price] = result
    return result


def find_user(users, user_id):
    for user in users:
        if user.id = user_id:  # BUG: assignment instead of comparison, also a syntax error
            return user
    return None


def divide(a, b):
    return a / b  # BUG: no handling for b == 0


def is_adult(age):
    if age > 18:  # BUG: off-by-one, 18-year-olds should count as adults
        return True
    return False


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append(item * quantity)  # BUG: should append (item, quantity) or similar, not multiply

    def total(self):
        return sum(self.items)


def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return items  # BUG: returns original list instead of deduplicated result
