from smartphone import Smartphone

# Создаем список catalog
catalog = [
    Smartphone("Samsung", "Galaxy S21", "+79123456789"),
    Smartphone("Apple", "iPhone 13", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"),
    Smartphone("Google", "Pixel 6", "+79456789012"),
    Smartphone("OnePlus", "9 Pro", "+79567890123")
]

# Выводим весь каталог в нужном формате
for phone in catalog:
    print(phone)
