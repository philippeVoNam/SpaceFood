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
from resources.global_file_paths import ingredientBankFilePath

# * Code
controller = IngredientController(ingredientBankFilePath)

ingredientsFilePath = "ingredients_input.csv"
with open(ingredientsFilePath, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        name = row[0]
        calories = int(row[1])

        if row[2].strip() == "p":
            type_ = SizeType.Per100g.value
        else:
            type_ = SizeType.Unit.value

        ingredient = Ingredient(name, calories, type_)

        controller.append(ingredient)
