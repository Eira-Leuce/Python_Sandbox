sale_price = int(input("Введите сумму продажи: "))

if sale_price == 0:
    print(f"Нерелевантная цена!")
elif 5000 >= sale_price > 0:
    discount = sale_price * 5 / 100
    new_sale_price = sale_price - discount
    print(f"Скидка: {discount}, сумма с учетом скидки: {new_sale_price}")
elif 15000 >= sale_price > 5000:
    discount = sale_price * 12 / 100
    new_sale_price = sale_price - discount
    print(f"Скидка: {discount}, сумма с учетом скидки: {new_sale_price}")
elif 25000 >= sale_price > 15000:
    discount = sale_price * 20 / 100
    new_sale_price = sale_price - discount
    print(f"Скидка: {discount}, сумма с учетом скидки: {new_sale_price}")
elif sale_price > 25000:
    discount = sale_price * 30 / 100
    new_sale_price = sale_price - discount
    print(f"Скидка: {discount}, сумма с учетом скидки: {new_sale_price}")
else:
    print(f"Нерелевантная цена!")