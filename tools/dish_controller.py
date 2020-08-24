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

        if not os.path.exists(dishFolderPathObj):
            os.makedirs(dishFolderPathObj)

            # Creating the data yaml file
            dishData = {
                'name': dish.name,
                'category': dish.category,
                'description': dish.description,
                'ingredients': dish.ingredients,
                'calories': dish.calories,
                'healthiness': dish.healthiness,
            }

            dishDataFilePath = dishFolderPathObj / "data.yaml"
            with open(dishDataFilePath, 'w') as file:
                yaml.dump(dishData, file)

            # Copy the image
            dishImageFilePathDest = dishFolderPathObj / "dish.jpg"
            shutil.copyfile(dish.dishImageFilePath, dishImageFilePathDest)

        else:
            print("dish " + dish.name + " already exists !")

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

                name = dishData.name
                category = dishData.category
                description = dishData.description
                ingredients = dishData.ingredients
                calories = dishData.calories
                healthiness = dishData.healthiness

                dishImageFilePath = str(Path(dishesFolderPath) / "dish.jpg")

                dish = Dish(name, category, description, ingredients, calories, healthiness, dishImageFilePath)

                return dish

        except Exception as e:
            print(e)
