from application.my_app import return_string


def test_return_string():
    res = return_string(1)
    assert res == '1'
