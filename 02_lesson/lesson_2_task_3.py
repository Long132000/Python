def square(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Сторона квадрата должна быть числом.")
    if side < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной.")

    area = side * side
    return int(area) + (1 if area != int(area) else 0)


def calculate_square_area():

    while True:
        try:
            side = float(input("Введите сторону квадрата: "))
            if side >= 0:
                break
            else:
                print("Сторона квадрата не может быть отрицательной.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

    try:
        area = square(side)
        print(f"Площадь квадрата: {area}")
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")


# Запуск функции
calculate_square_area()
