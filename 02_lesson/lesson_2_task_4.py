def fizz_buzz():
    while True:
        try:
            n = int(input("Введите целое число больше 0: "))
            if n > 0:
                break
            else:
                print("Число должно быть больше 0.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i)


fizz_buzz()
