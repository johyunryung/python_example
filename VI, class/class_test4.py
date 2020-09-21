class Food:
    def __init__(self, name, price, flavor):
        self.name = name
        self.price = price
        self.flavour = flavor

    def __str__(self):
        return f'이름 : {self.name}, 가격 : {self.price}, 맛 : {self.flavor}'

    def get_price(self):
         return self.price

food1 = Food("로제파스타", 7900, "로제맛")
food2 = Food("알리오올리오",6900,"기름맛")
orders = [food1, food2]

total_price = 0
for order in orders:
    total_price += order.get_price()

print(total_price)