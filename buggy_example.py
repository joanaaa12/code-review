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


def calculate_average_grade(grades):
    return sum(grades) / len(grades)  # BUG: no handling for empty list, ZeroDivisionError


def is_palindrome(text):
    return text == text.reverse()  # BUG: strings have no .reverse() method, should use text[::-1]


def get_last_n_items(items, n):
    return items[-n:]  # BUG: when n == 0, -n is 0 and returns the whole list instead of an empty one


def merge_dicts(dict1, dict2):
    result = dict1  # BUG: aliases dict1 instead of copying it, mutates caller's dict
    for key, value in dict2.items():
        result[key] = value
    return result


def count_occurrences(items, target):
    count = 0
    for item in items:
        if item == target:
            count = count + 1
        return count  # BUG: return is inside the loop, exits after first iteration


class Counter:
    count = 0  # BUG: class attribute shared across all instances instead of per-instance state

    def increment(self):
        self.count += 1
        return self.count
