 # * author : Philippe Vo 
 # * date : Sep-07-2020 23:10:06
 
# * Imports
# 3rd Party Imports
from pathlib import Path
import os
# User Imports
from resources.global_file_paths import ingredientBankFilePath, inventoryFilePath, dishesFolderPath
from tools.inventory_controller import InventoryController
from tools.dish_controller import DishController

# * Code
class FoodButler():
    """
    food bulter is here to take of all your eating needs
    """
    def __init__(self):
        """ init. """
        # inits.
        self.inventoryController = InventoryController(inventoryFilePath)
        self.dishController = DishController()

    def scan_available_dishes(self, category):
        """
        scan all the dishes in category and returns the dishes that you make

        Arguments
        ---------
        category : elements.enums.DishCategories
            dish category
        """
        categoryDishesFolderPath = Path(dishesFolderPath) / category
        dishesFolderNames = os.listdir(categoryDishesFolderPath)

        # load all the dishes from category
        loadedDishes = []
        for dishFolderName in dishesFolderNames:
            dishFolderPath = categoryDishesFolderPath / dishFolderName

            dish = self.dishController.read(dishFolderPath)
            loadedDishes.append(dish)

        # load inventory
        componentsAvailable = self.inventoryController.load()
        ingredientsAvailableNames = []
        for component in componentsAvailable:
            ingredientsAvailableNames.append(component.ingredient.name)

        # scan for available dishes
        availableDishes = []
        for dish in loadedDishes:
            dishAvailableFlag = True
            for component in dish.components:
                if component.ingredient.name not in ingredientsAvailableNames:
                    print("missing -> ", component.ingredient.name)
                    dishAvailableFlag = False
                    continue

                else:
                    for componentAv in componentsAvailable:
                        if component.ingredient.name == componentAv.ingredient.name:
                            if component.quantity > componentAv.quantity:
                                print("not enough -> ", component.ingredient.name)
                                dishAvailableFlag = False
                                break

            if dishAvailableFlag:
                availableDishes.append(dish)

        for dish in availableDishes:
            print(dish.name)
