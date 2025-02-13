class Smartphone:
    # Конструктор класса, принимающий марку, модель и номер телефона
    def __init__(self, brand, model, phone_number):
        self.brand = brand          # Марка телефона
        self.model = model          # Модель телефона
        self.phone_number = phone_number  # Абонентский номер

    # Метод для вывода информации о телефоне
    def __str__(self):
        return f"{self.brand} - {self.model}. {self.phone_number}"
