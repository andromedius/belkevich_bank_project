list_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
             ]


def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая возвращает новый список словарей с ключом state:'EXECUTED' """

    return [i for i in list_dict if i["state"] == state]


print(filter_by_state(list_dict, "EXECUTED"))


def sort_by_date(list_dict: list[dict], date_sort: bool = True) -> list[dict]:
    """Функция берет список операций и сортирует по дате по убыванию"""

    list_sort_by_date = sorted(list_dict, key=lambda x: x["date"], reverse=date_sort)

    return list_sort_by_date


print(sort_by_date(list_dict, True))
