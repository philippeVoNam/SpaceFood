 # * author : Philippe Vo 
 # * date : Sep-07-2020 13:42:13
 
# * Imports
# 3rd Party Imports
import yaml
import csv
# User Imports
from elements.enums import SizeType
from elements.ingredient import Ingredient
from tools.ingredient_controller import IngredientController
from elements.dish import Dish
from tools.dish_controller import DishController
from elements.enums import DishCategories, Healthiness
from elements.component import Component
from tools.inventory_controller import InventoryController
from resources.global_file_paths import ingredientBankFilePath, inventoryFilePath

# * Code
ingredientController = IngredientController(ingredientBankFilePath)
controller = InventoryController(inventoryFilePath)

ingredientsFilePath = "inventory_input.csv"
with open(ingredientsFilePath, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        name = row[0]
        quantity = int(row[1])

        try:
            ingredient = ingredientController.read(name)

            component = Component(ingredient, quantity)

            controller.append(component)

        except:
            print("error occured")
