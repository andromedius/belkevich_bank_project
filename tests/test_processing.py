import pytest

from src.processing import filter_by_state, sort_by_date

list_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
             ]
"""Список с полноценными словарями"""

list_dict_same_dates = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
                        ]
"""Список со словарями с одинаковыми датами"""

list_dict_1 = [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
               ]
"""Список со словарями с state: CANCELED"""

list_dict_2 = [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03'},
               {'id': 939719570, 'state': 'CANCELED', 'date': '2018-0'},
               {'id': 594226727, 'state': 'CANCELED', 'date': 'T21:27:25.241689'},
               {'id': 615064591, 'state': 'CANCELED', 'dte': ''}
               ]
"""Список с некорректным ключом date"""

list_dict_3 = [{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
               {'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
               {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}
               ]
"""Список без ключа state"""


def test_filter_by_state(list_dict_right):
    """Тестирование фильтрации списка словарей"""

    assert filter_by_state(list[dict](list_dict), "EXECUTED") == list_dict_right
    assert filter_by_state(list[dict](list_dict_1), "EXECUTED") == []
    assert filter_by_state(list_dict_2) == []
    with pytest.raises(KeyError):
        assert filter_by_state(list_dict_3)


def test_sort_by_date(sort_by_date_right):
    """Тестирование сортировки по дате"""
    assert sort_by_date(list_dict) == sort_by_date_right


def test_sort_by_date_2(sorted_by_date):
    """Тестирование сортировки по дате для случаев:
     1.reverse-False;
     2.Список со словарями с некорректным ключом date"""
    assert sort_by_date(list_dict, False) == sorted_by_date

    with pytest.raises(KeyError):
        assert sort_by_date(list_dict_2)


def test_sort_by_date_same(sorted_same_dates):
    """Тестирование списка с одинаковыми датами"""
    assert sort_by_date(list_dict_same_dates) == sorted_same_dates
