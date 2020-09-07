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
    def __init__(self, name, category, description, components, healthiness, dishImageFilePath):
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
        components : [[Ingredient, quantity], ...]
            list of ingredients (elements.ingredient) + their quantity
        calories : int
            number of calories
        healthiness : str (fattening, neutral, healthy) (enum from Healthiness)
            healthiness of the dish
        """

        self.name = name
        self.category = category
        self.description = description
        self.components = components
        self.calories = self.calories_cal(components)
        self.healthiness = healthiness
        self.dishImageFilePath = dishImageFilePath

        self.dishFolderPath = str(Path(dishesFolderPath) / category / self.name)

    def calories_cal(self, components):
        """
        calculate the number of calories in the dish

        Arguments
        ---------
        components : [[Ingredient, quantity], ...]
            list of ingredients (elements.ingredient) + their quantity
        """
        totalCalories = 0
        for component in components:
            ingredient = component[0]
            quantity = int(component[1])

            calories = ingredient.caloriesMultiplier * quantity

            totalCalories = calories + totalCalories

        return totalCalories


    def __str__(self):
        componentData = []
        for component in self.components:
            ingredient = component[0]
            quantity = component[1]
            componentBuild = [ingredient.pickle_it(), quantity]

            componentData.append(componentBuild)

        data = [self.name, self.category, self.description, componentData, self.calories, self.healthiness]
        return str(data)
