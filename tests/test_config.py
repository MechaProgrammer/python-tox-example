from application import config


def test_add_values():
    res = config.add_numbers(1, 1)
    assert res == 2
