import pytest

from src.widget import mask_account_card, get_date

# from src.masks import get_mask_card_number, get_mask_account


def test_mask_account_card():
    assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'



def test_mask_account_card_1(right_account_card):
    assert mask_account_card('Visa Platinum 7000792289606361') == right_account_card



@pytest.mark.parametrize('value, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361')]
                         )
def test_mask_account_card(value, expected):
    assert expected == mask_account_card(value)


def test_get_date():
    assert get_date('2024-03-11Т02:26:18.671407') == '11.03.2024'
