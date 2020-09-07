import yaml
from elements.enums import SizeType
from elements.ingredient import Ingredient
from tools.ingredient_controller import IngredientController
from elements.dish import Dish
from tools.dish_controller import DishController
from elements.enums import DishCategories, Healthiness
from elements.component import Component
from tools.inventory_controller import InventoryController

controller = InventoryController("inventory.yaml")

steak = Ingredient("steak",100, SizeType.Unit.value)
lobster = Ingredient("lobster",200, SizeType.Unit.value)

steakCp = Component(steak, 2)
lobsterCp = Component(lobster, 3)

controller.append(steakCp)
controller.append(lobsterCp)

lobsterCp = Component(lobster, 5)

controller.remove("steak")
controller.edit(lobsterCp)

# components = [[steak,1], [lobster, 2]]
# dish = Dish("l-s", DishCategories.Dinner.value, "amazing", components, Healthiness.Fatenning.value, "img.jpg")

# dishController = DishController()
# # dishController.create(dish)
# dish = dishController.read("data/dishes/dinner/l-s")
# print(dish)
