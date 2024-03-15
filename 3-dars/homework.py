class Shop:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.products = {}

    def add_product(self, product_name, price):
        if product_name not in self.products:
            self.products[product_name] = price
            print(f"Товар \"{product_name}\" успешно добавлен в магазин по цене {price}.")
        else:
            print("Ошибка: Товар с таким названием уже есть в магазине.")

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            print(f"Товар \"{product_name}\" успешно удален из магазина.")
        else:
            print("Ошибка: Товар с таким названием отсутствует в магазине.")

    def sell_product(self, product_name, quantity):
        if product_name in self.products:
            if quantity > 0 and quantity <= self.products[product_name]:
                total_price = self.products[product_name] * quantity
                self.products[product_name] -= quantity
                print(f"Продано {quantity} единиц товара \"{product_name}\". Общая стоимость продажи: {total_price}.")
            else:
                print("Ошибка: Недостаточное количество товара для продажи.")
        else:
            print("Ошибка: Товар с таким названием отсутствует в магазине.")


shop = Shop("Мой магазин", "Улица Пушкина, дом Колотушкина")

shop.add_product("Яблоки", 50)
shop.add_product("Бананы", 70)

shop.sell_product("Яблоки", 10)
shop.sell_product("Бананы", 5)

shop.remove_product("Яблоки")
shop.remove_product("Мандарины")
