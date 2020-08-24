 # * author : Philippe Vo 
 # * date : Aug-23-2020 18:53:19
 
# * Imports
# 3rd Party Imports
from pathlib import Path
# User Imports
from resources.global_file_paths import dishesFolderPath

# * Code
class Dish():
    """
    class that represents a dish
    """
    def __init__(self, name, category, description, ingredients, calories, healthiness, dishImageFilePath):
        """
        init.

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

        self.name = name
        self.category = category
        self.description = description
        self.ingredients = ingredients
        self.calories = calories
        self.healthiness = healthiness
        self.dishImageFilePath = dishImageFilePath

        self.dishFolderPath = str(Path(dishesFolderPath) / "dishes" / category)
