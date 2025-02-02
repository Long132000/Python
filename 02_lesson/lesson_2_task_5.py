def month_to_season(month):
    if not isinstance(month, int):
        return "Ошибка: Номер месяца должен быть целым числом."
    if not 1 <= month <= 12:
        return "Ошибка: Номер месяца должен быть от 1 до 12."

    if 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Зима"


def get_season_from_user():
    while True:
        try:
            month = int(input("Введите номер месяца (1-12): "))
            season = month_to_season(month)
            print(f"Сезон для месяца {month}: {season}")
            break
        except ValueError:
            print("Ошибка! Введите целое число.")


get_season_from_user()
