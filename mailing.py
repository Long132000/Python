class Mailing:
    # Конструктор класса, принимающий адреса, стоимость и трек-номер
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address      # Адрес получателя (тип Address)
        self.from_address = from_address  # Адрес отправителя (тип Address)
        self.cost = cost                  # Стоимость (число)
        self.track = track                # Трек-номер (строка)

    # Метод для вывода информации о почтовом отправлении
    def __str__(self):
        return (
            f"Отправление {self.track} из {self.from_address.index}, "
            f"{self.from_address.city}, {self.from_address.street}, "
            f"{self.from_address.house} - {self.from_address.apartment} в "
            f"{self.to_address.index}, {self.to_address.city}, "
            f"{self.to_address.street}, {self.to_address.house} - "
            f"{self.to_address.apartment}. Стоимость {self.cost} рублей."
        )
