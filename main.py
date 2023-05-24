# Задача №55.  Создать телефонный справочник с возможностью импорта
# и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.

# 1. Програм33
# ма должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для
# поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
import functions


while True:
    print('1. вывод, 2. добавление, 3. поиск')
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    else:
        break
