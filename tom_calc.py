from decimal import Decimal as D
from bisect import bisect

TWOPLACES = D(10) ** -2


def amount(price, quantity):
    return D(price * quantity).quantize(TWOPLACES)


def discount(amount):
    breakpoints = [1000, 5000, 7000, 10000, 50000]
    discounts = [D('0'), D('3'), D('5'), D('7'), D('10'), D('15')]
    return discounts[bisect(breakpoints, amount)]


def tax(state):
    taxes = {
        'UT': D('6.85'),
        'NV': D('8'),
        'TX': D('6.28'),
        'AL': D('4'),
        'CA': D('8.25')
    }
    return taxes[state]


def discounted_amount(amount):
    return D(amount * (1 - (discount(amount) / 100)))


def discounted_taxed_amount(amount, state):
    return (discounted_amount(amount) * (1 + tax(state) / 100)).quantize(TWOPLACES)


def calculate(price, quantity, state):
    return discounted_taxed_amount(amount(price, quantity), state)
