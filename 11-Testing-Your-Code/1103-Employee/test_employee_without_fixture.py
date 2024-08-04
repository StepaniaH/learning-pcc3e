from employee import Employee


def test_give_default_raise():
    assert Employee("John", "Doe", 10000).give_raise() == 15000


def test_give_custom_raise():
    assert Employee("John", "Doe", 10000).give_raise(
        raise_amount=1000) == 11000
