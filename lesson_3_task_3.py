from address import Address
from mailing import Mailing

# Создаем экземпляры класса Address для отправителя и получателя
to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "12")

# Создаем экземпляр класса Mailing
mailing = Mailing(to_address, from_address, 500, "ABC123")

# Выводим информацию о почтовом отправлении
print(mailing)
