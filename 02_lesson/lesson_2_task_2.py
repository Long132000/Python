def is_year_leap(year):
    if not isinstance(year, int):
        raise TypeError("Год должен быть целым числом.")
    return year % 4 == 0


def check_leap_year():
    while True:
        try:
            year = int(input("Введите год: "))
            break

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    try:
        result = is_year_leap(year)
        print(f"Год {year}: {result}")

    except TypeError as e:
        print(f"Ошибка: {e}")


check_leap_year()
