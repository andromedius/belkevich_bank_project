from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number('1234567887654321') == '1234 56** **** 4321'


def test_get_mask_card_number_empty():
    assert get_mask_card_number('') == 'Отсутствует номер карты'


def test_get_mask_card_number_more_num():
    assert get_mask_card_number('123456789987654321') == 'Неправильный номер карты'


def test_get_mask_card_number_less_num():
    assert get_mask_card_number('12345677654321') == 'Неправильный номер карты'


def test_get_mask_account():
    assert get_mask_account('12345678900987654321') == '** 4321'


# def test_get_mask_card_number_empty():
#     assert get_mask_card_number('') == 'Отсутствует номер карты'
#
#
# def test_get_mask_card_number_more_num():
#     assert get_mask_card_number('123456789987654321') == 'Неправильный номер карты'
#
#
# def test_get_mask_card_number_less_num():
#     assert get_mask_card_number('12345677654321') == 'Неправильный номер карты'