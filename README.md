# Проект "Банковские операции"

## Описание:

Проект "Банковские операции" - Это виджет на Python для презжентации нескольих последних
успешных банковских операций клиента. 

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:andromedius/Belkevich_bank_project.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```
## Иcпользование

1. Функция маскировки номера банковской карты
get_mask_card_number

Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску. 
Номер карты замаскирован и отображается в формате 
XXXX XX** **** XXXX, где 
X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы 
отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами. 
Пример работы функции:
7000792289606361     # входной аргумент
7000 79** **** 6361


2. Функция маскировки номера банковского счета 
get_mask_account

Функция get_mask_account принимает на вход номер счета и возвращает его маску. 
Номер счета замаскирован и отображается в формате 
**XXXX, где 
X — это цифра номера. То есть видны только последние 4 цифры номера, 
а перед ними — две звездочки. Пример работы функции:
73654108430135874305  # входной аргумент
**4305  # выход функции

3. функция обработки информации о картах и о счетах 
mask_account_card

Функция принимает один аргумент — строку, содержащую тип и номер карты или счета.
Аргументом может быть строка типа :
Visa Platinum 7000792289606361, или 
Maestro 7000792289606361, или 
Счет 73654108430135874305
Возвращает строку с замаскированным номером. Для карт и счетов используйте разные типы маскировки. 

4. Функция обработки формата даты get_date

Функция принимает на вход строку с датой в формате: "2024-03-11T02:26:18.671407", и возвращает 
строку с датой в формате: "ДД.ММ.ГГГГ".
 ("11.03.2024").

5. Функция sort_by_date

Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по
умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате 

## Тестирование

Проект содержит тесты ко всем функциям проекта. Модули тестируются в отдельных тестовых файлах.
Запуск тестов осуществляется командой в терминале:
```
pytest
```

## Лицензия:

Проект лицензирован по [лицензии Apache License 2.0] (LICENSE)
