from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """ Функция, которая маскирует номер счета или карты"""
    text_result = ""
    digit_result = ""
    digit_count = 0

    for el in type_and_number:
        # if el.isalpha():
        # text_result += el
        if el.isdigit():
            digit_result += el
            digit_count += 1
        else:
            text_result += el
    if digit_count == 20:
        display_massage = f"{text_result}{get_mask_account(digit_result)}"
    elif digit_count == 16:
        display_massage = f"{text_result}{get_mask_card_number(digit_result)}"
    else:
        display_massage = 'Неправильный номер'
    return display_massage


def get_date(date_of_operation: str) -> str:
    """ Функция, которая возвращает строку с датой в формате ДД.ММ.ГГГГ"""

    return date_of_operation[8:10] + "." + date_of_operation[5:7] + "." + date_of_operation[0:4]
