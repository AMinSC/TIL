from solid_principles import *


chicken = FoodStore("BBQ", 10, 22)
print(chicken.register_store())

pizza = Menu("BBQ", 10, 22, "gold_olive_chicken", 20000)
print(pizza.menu_registration(3))
print(pizza.menu_remove("gold_olive_chicken"))

test = Order("BBQ", 10, 22, "gold_olive_chicken", 20000)
print(test.order_menu(3))
