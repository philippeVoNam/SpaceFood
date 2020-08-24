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

# * Code
class DishController():
    """
    utility class that provides the ability to: create, edit and delete -> dishes (works with the yaml file of the dish)
    """
    def __init__(self):
        """ init. """
        pass

    def create(self, name, category, description, ingredients, calories, healthiness, dishImageFilePath):
        """
        creates a dish by :
        - creating a directory for that dish inside the appropriate category (breakfast, lunch, dinner, etc.)
        - creating a data.yaml with the input parameters given
        - copying the image file to dish dir

        Arguments
        ---------
        name : str
            name of the dish
        category : str (breakfast, lunch, dinner, snacks) (enum from DishCategories)
            category of dish
        description : str
            description of the dish
        ingredients : [Ingredients]
            list of ingredients (elements.ingredient)
        calories : int
            number of calories
        healthiness : str (fattening, neutral, healthy) (enum from Healthiness)
            healthiness of the dish
        """
        # Creating dir of dish
        dishesFolderPathObj = Path(dishesFolderPath)
        dishFolderPathObj = dishesFolderPathObj  / category / name

        if not os.path.exists(dishFolderPathObj):
            os.makedirs(dishFolderPathObj)

            # Creating the data yaml file
            dish = {
                'name': name,
                'category': category,
                'description': description,
                'ingredients': ingredients,
                'calories': calories,
                'healthiness': healthiness,
            }

            dishDataFilePath = dishFolderPathObj / "data.yaml"
            with open(dishDataFilePath, 'w') as file:
                yaml.dump(dish, file)

            # Copy the image
            dishImageFilePathDest = dishFolderPathObj / "dish.jpg"
            shutil.copyfile(dishImageFilePath, dishImageFilePathDest)

        else:
            print("dish " + name + " already exists !")
