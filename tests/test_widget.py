import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    """Тест корректного распознавания типа маскировки"""
    assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'


def test_mask_account_card_1(right_account_card):
    """Тест корректного распознавания типа маскировки"""
    assert mask_account_card('Visa Platinum 7000792289606361') == right_account_card


@pytest.mark.parametrize('value, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет ** 4305'),
    ('Счет 64686473678894779589', 'Счет ** 9589')]
                         )
def test_mask_account_card_2(value, expected):
    """Тест корректного распознавания типа маскировки"""
    assert expected == mask_account_card(value)


def test_get_date():
    """Тестирование правильности преобразования даты"""
    assert get_date('2024-03-11Т02:26:18.671407') == '11.03.2024'
