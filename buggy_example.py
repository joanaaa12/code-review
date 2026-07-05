"""Small utility module with several intentionally planted bugs, used to test code review."""


def average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)


def get_discounted_price(price, discount_percent=10, cache=None):
    if cache is None:
        cache = {}
    if price in cache:
        return cache[price]
    result = price - (price * discount_percent / 100)
    cache[price] = result
    return result


def find_user(users, user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_adult(age):
    if age >= 18:
        return True
    return False


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def total(self):
        return sum(price * quantity for price, quantity in self.items)


def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def calculate_average_grade(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def is_palindrome(text):
    return text == text[::-1]


def get_last_n_items(items, n):
    if n <= 0:
        return []
    return items[-n:]


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = value
    return result


def count_occurrences(items, target):
    count = 0
    for item in items:
        if item == target:
            count = count + 1
    return count


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
