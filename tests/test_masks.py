import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number('1234567887654321') == '1234 56** **** 4321'


def test_get_mask_card_number_empty():
    assert get_mask_card_number('') == 'Отсутствует номер карты'


def test_get_mask_card_number_more_num():
    assert get_mask_card_number('123456789987654321') == 'Неправильный номер карты'


def test_get_mask_card_number_less_num():
    assert get_mask_card_number('12345677654321') == 'Неправильный номер карты'


def test_get_mask_card_number_let():
    assert get_mask_account('1234567vv7654321') == 'Неправильный номер счёта'


def test_get_mask_account():
    assert get_mask_account('12345678900987654321') == '** 4321'


def test_get_mask_account_empty():
    assert get_mask_account('') == 'Отсутствует номер счёта'


def test_get_mask_account_more_num():
    assert get_mask_account('1234567890110987654321') == 'Неправильный номер счёта'


def test_get_mask_account_less_num():
    assert get_mask_account('12345677654321') == 'Неправильный номер счёта'


def test_get_mask_account_let():
    assert get_mask_account('1234567vv7654321') == 'Неправильный номер счёта'


@pytest.mark.parametrize('value, expected',[
    ('', 'Отсутствует номер счёта'),
    ('1234567890123456', 'Неправильный номер счёта'),
    ('12345678901234567890', '** 7890'),
    ('1234567891230', 'Неправильный номер счёта')
])
def test_get_mask_account_some(value, expected):
    assert get_mask_account(value) == expected


def test_get_mask_account_fix(bank_account):
    assert get_mask_account('12345678900987651234') == bank_account