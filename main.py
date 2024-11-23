from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

list_dict_2 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
               ]


if __name__ == '__main__':
    print(mask_account_card('Visa Platinum 7000794028906361'))
    print(get_date(str('2018-06-30T02:08:58.425572')))
    print(filter_by_state(list[dict](list_dict_2), "EXECUTED"))
    print(sort_by_date(list[dict](list_dict_2), True))
    print(mask_account_card('Visa Platinum 7000792289606361'))
    print(get_date('2024-03-11Т02:26:18.671407'))
