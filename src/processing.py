list_dict_2 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
                   ]


def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая возвращает новый список словарей с ключом state:'EXECUTED' """

    return [i for i in list_dict if i["state"] == state]


print(filter_by_state(list[dict](), "EXECUTED"))


def sort_by_date(list_dict: list[dict], date_sort: bool = True) -> list[dict]:
    """Функция берет список операций и сортирует по дате по убыванию"""


    list_sort_by_date = sorted(list_dict, key=lambda x: x["date"], reverse=date_sort)

    return list_sort_by_date


print(sort_by_date(list[dict](list_dict_2), True))
