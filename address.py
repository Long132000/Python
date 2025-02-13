class Address:
    # Конструктор класса, принимающий индекс, город, улицу, дом и квартиру
    def __init__(self, index, city, street, house, apartment):
        self.index = index    # Индекс
        self.city = city      # Город
        self.street = street  # Улица
        self.house = house    # Дом
        self.apartment = apartment  # Квартира
