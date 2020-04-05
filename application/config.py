"""Configure something"""


def add_numbers(*args):
    """Add numbers"""
    total = 0
    for arg in args:
        total += arg
    return total
