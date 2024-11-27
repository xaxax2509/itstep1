# Фіксовані курси валют (можна замінити актуальними значеннями)
exchange_rates = {
    "UAH": 1,
    "USD": 41,
    "EUR": 43,}


# Функція для конвертації валюти в гривні
def convert_to_uah(amount, currency):
    if currency in exchange_rates:
        rate = exchange_rates[currency]  # Отримуємо курс валюти
        converted_amount = amount * rate  # Перераховуємо в гривні
        return round(converted_amount, 2)  # Повертаємо результат, округлений до 2 знаків
    else:
        return "Невірна валюта"  # Якщо валюта не знайдена


# Запитуємо користувача на введення
amount = float(input("Введіть кількість вашої валюти: "))
currency = input("Введіть код вашої валюти (UAH, USD, EUR): ").upper()

# Конвертуємо та виводимо результат
converted = convert_to_uah(amount, currency)

# Виводимо результат
if isinstance(converted, float):
    print(f"{amount} {currency} = {converted} UAH")
else:
    print(converted)  # Вивести помилку, якщо валюта неправильна


