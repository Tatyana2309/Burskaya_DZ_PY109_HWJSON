import json

# task 1

purchase = []
while True:
    purchase_name = input("Введите название Вашей покупки: ") # пользователь вводит название покупки
    if purchase_name == 'стоп':
        break # при вводе слова стоп, останавливается ввод
    purchase_price = int(input("Введите стоимость Вашей покупки: ")) # пользователь вводит стоимость покупки
    purchase.append({'название': purchase_name,
                     'стоимость': purchase_price}) # соединяем все покупки в список со значением словарь

    with open('purchase.json', 'w', encoding='UTF-8') as file: # записываем данные в файл json
        json.dump(purchase, file, ensure_ascii=False)

#task 2

with open('purchase.json', encoding='UTF-8') as file: # открываем файл json
    data = json.load(file)
    sum_price = 0
    for i in data: # циклом разбиваем на отдельные данные
        sum_price += int(i['стоимость']) # находим сумму значений ключа стоимость из словаря
    print(f'Сумма всех покупок равна: {sum_price}')
