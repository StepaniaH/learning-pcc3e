import pytest
from employee import Employee


@pytest.fixture
def employee():
    return Employee("John", "Doe", 10000)


def test_give_default_raise(employee):
    assert employee.give_raise() == 15000


def test_give_custom_raise(employee):
    assert employee.give_raise(raise_amount=1000) == 11000
