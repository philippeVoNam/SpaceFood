 # * author : Philippe Vo 
 # * date : Aug-22-2020 15:06:54
 
# * Imports
# 3rd Party Imports
import yaml
import os
import shutil
from pathlib import Path
# User Imports
from resources.global_file_paths import dishesFolderPath
from elements.dish import Dish
from elements.ingredient import Ingredient
from elements.component import Component
from resources.global_file_paths import dishesFolderPath

# * Code
class DishController():
    """
    utility class that provides the ability to: create, edit and delete -> dishes (works with the yaml file of the dish)
    """
    def __init__(self):
        """ init. """
        pass

    def create(self, dish):
        """
        creates a dish by :
        - creating a directory for that dish inside the appropriate category (breakfast, lunch, dinner, etc.)
        - creating a data.yaml with the input parameters given
        - copying the image file to dish dir

        Arguments
        ---------
        dish : elements.Dish
            dish to be created
        """
        # Creating dir of dish
        dishFolderPathObj = Path(dish.dishFolderPath)

        resultFlag = False
        if not os.path.exists(dishFolderPathObj):
            os.makedirs(dishFolderPathObj)

            # Creating the data yaml file
            dishData = dish.pickle_it()

            dishDataFilePath = dishFolderPathObj / "data.yaml"
            with open(dishDataFilePath, 'w') as file:
                yaml.dump(dishData, file)

            # Copy the image
            dishImageFilePathDest = dishFolderPathObj / "dish.jpg"
            shutil.copyfile(dish.dishImageFilePath, dishImageFilePathDest)

            print(str(dishFolderPathObj) + " created !")
            resultFlag = True

        else:
            print("dish " + dish.name + " already exists !")
            resultFlag = False

        return resultFlag

    def read(self, dishFolderPath):
        """
        read the dish from folderPath and retrieve its information

        Arguments
        ---------
        dishFolderPath : str
            path to the folder of the dish
        """
        dishFilePathData = str(Path(dishFolderPath) / "data.yaml")

        try:
            with open(dishFilePathData) as file:
                dishData = yaml.load(file, Loader = yaml.FullLoader)

                name = dishData["name"]
                category = dishData["category"]
                description = dishData["description"]

                componentsData = dishData["components"]
                components = []
                for component in componentsData:
                    ingredientCp = component["ingredient"]
                    ingredient = Ingredient(ingredientCp["name"], int(ingredientCp["calories"]), ingredientCp["type_"])
                    quantity = int(component["quantity"])

                    component = Component(ingredient, quantity)
                    components.append(component)

                calories = dishData["calories"]
                healthiness = dishData["healthiness"]

                dishImageFilePath = str(Path(dishFolderPath) / "dish.jpg")

                dish = Dish(name, category, description, components, healthiness, dishImageFilePath)

                return dish

        except Exception as e:
            print(e)

    def remove(self, dishFolderPath):
        """
        remove the dish from data folder

        Arguments
        ---------
        dishFolderPath : str
            path to the dish
        """
        dishFolderPath = Path(dishFolderPath)

        if os.path.exists(dishFolderPath):
            os.rmdir(dishFolderPath)

        else:
            print(dishFolderPath + " does not exist !")

    def load_all(self):
        """
        load all the dishes in and returns a list of dishes
        """
        breakfastDishesPath = Path(dishesFolderPath) / "breakfast"
        lunchDishesPath = Path(dishesFolderPath) / "lunch"
        dinnerDishesPath = Path(dishesFolderPath) / "dinner"
        snacksDishesPath = Path(dishesFolderPath) / "snacks"

        breakfastDishesPaths = self.merge_files_path(breakfastDishesPath)
        lunchDishesPaths = self.merge_files_path(lunchDishesPath)
        dinnerDishesPaths = self.merge_files_path(dinnerDishesPath)
        snacksDishesPaths = self.merge_files_path(snacksDishesPath)

        dishes = []
        for dishesFolder in [breakfastDishesPaths, lunchDishesPaths, dinnerDishesPaths, snacksDishesPaths]:
            for dishPath in dishesFolder:
                dish = self.read(dishPath)

                dishes.append(dish)

        return dishes

    def merge_files_path(self, parentDir):
        """
        given a dir, merge all the files with the parentDir to create its full path
        """
        files = os.listdir(parentDir)

        filePaths = []
        for file_ in files:
            filePath = os.path.join(parentDir, file_)

            filePaths.append(filePath)

        return filePaths
