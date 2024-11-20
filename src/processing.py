def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая возвращает новый список словарей с ключом state:'EXECUTED' """

    return [i for i in list_dict if i["state"] == state]


def sort_by_date(list_dict: list[dict], date_sort: bool = True) -> list[dict]:
    """Функция берет список операций и сортирует по дате по убыванию"""

    list_sort_by_date = sorted(list_dict, key=lambda x: x["date"], reverse=date_sort)

    return list_sort_by_date
