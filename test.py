from elements.dish import Dish
from elements.enums import SizeType
from elements.ingredient import Ingredient
from tools.ingredient_controller import IngredientController
from elements.dish import Dish
from tools.dish_controller import DishController
from elements.enums import DishCategories, Healthiness
from elements.component import Component
from tools.inventory_controller import InventoryController
from tools.food_butler import FoodButler

name = "wonton noodle soup"
category = DishCategories.Lunch.value
description = '''
Wonton noodle soup is a soup that consists of broth and noodles and wontons.
'''
components = []

controller = IngredientController("data/ingredients_bank.yaml")
shrimp = controller.read("shrimp")
wontonNoodle = controller.read("wonton noodle")
charSiu = controller.read("char siu")

shrimpCp = Component(shrimp, 100)
wontonNoodleCp = Component(wontonNoodle, 300)
charSiuCp = Component(charSiu, 50)

components.append(shrimpCp)
components.append(wontonNoodleCp)
components.append(charSiuCp)

healthiness = Healthiness.Neutral.value
dishImageFilePath = "img.jpg"
dish = Dish(name, category, description.strip(), components, healthiness, dishImageFilePath)

controllerDish = DishController()
# controllerDish.create(dish)

butler = FoodButler()
butler.scan_available_dishes(DishCategories.Lunch.value)
