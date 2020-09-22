 # * author : Philippe Vo 
 # * date : Sep-06-2020 20:56:35
 
# * Imports
# 3rd Party Imports
import yaml
from pathlib import Path
# User Imports
from elements.ingredient import Ingredient

# * Code
class IngredientController():
    """
    class used to control the elements.Ingredient
    """
    def __init__(self, filePath):
        """ init. """
        # inits.
        self.filePath = Path(filePath)

    def append(self, ingredient):
        """
        add ingredient to Ingredients Bank

        Arguments
        ---------
        ingredient : elements.Ingredient
        """
        with open(self.filePath, 'r') as yamlfile:
            loadedData = yaml.safe_load(yamlfile) # Note the safe_load

            ingredientsNames = []
            for ingredientData in loadedData:
                ingredientsNames.append(ingredientData["name"].lower())

            data = ingredient.pickle_it() # turn ingredient to a dict representation

            resultFlag = False
            if data["name"].lower() not in ingredientsNames:
                loadedData.append(data)
                resultFlag = True

            else:
                print("ingredient already in")
                resultFlag = False

        if loadedData:
            with open(self.filePath,'w') as yamlfile:
                yaml.safe_dump(loadedData, yamlfile) # Also note the safe_dump

        return resultFlag

    def remove(self, ingredientName):
        """
        remove ingredient to Ingredients Bank

        Arguments
        ---------
        ingredientName : str
        """
        with open(self.filePath, 'r') as yamlfile:
            loadedData = yaml.safe_load(yamlfile) # Note the safe_load

            ingredientsNames = []
            for ingredientData in loadedData:
                ingredientsNames.append(ingredientData["name"].lower())

            if ingredientName.lower() in ingredientsNames:
                for ingredientData in loadedData:
                    if ingredientData["name"].lower() == ingredientName.lower():
                        loadedData.remove(ingredientData)

            else:
                print("ingredient not in bank")

        if loadedData:
            with open(self.filePath,'w') as yamlfile:
                yaml.safe_dump(loadedData, yamlfile) # Also note the safe_dump

    def edit(self, editedIngredient):
        """
        edit ingredient to Ingredients Bank

        Arguments
        ---------
        ingredient : elements.Ingredient
        """
        # remove the current ingredient
        self.remove(editedIngredient.name)

        # append the edited ingredient
        self.append(editedIngredient)

    def read(self, ingredientName):
        """
        read ingredient from the ingredients bank

        Arguments
        ---------
        ingredientName : str
            name of the ingredient

        Returns
        -------
        ingredient : elements.Ingredient
        """
        with open(self.filePath, 'r') as yamlfile:
            loadedData = yaml.safe_load(yamlfile) # Note the safe_load

            ingredientsNames = []
            for ingredientData in loadedData:
                ingredientsNames.append(ingredientData["name"].lower())

            if ingredientName.lower() in ingredientsNames:
                for ingredientData in loadedData:
                    if ingredientData["name"].lower() == ingredientName.lower():

                        name = ingredientData["name"]
                        calories = int(ingredientData["calories"])
                        type_ = ingredientData["type_"]

                        ingredient = Ingredient(name, calories, type_)

                        return ingredient

            else:
                print("ingredient not in bank")

    def get_names(self):
        """
        get all the ingredients name from the ingredient bank
        """
        with open(self.filePath, 'r') as yamlfile:
            loadedData = yaml.safe_load(yamlfile) # Note the safe_load

            ingredientsNames = []
            for ingredientData in loadedData:
                ingredientsNames.append(ingredientData["name"].lower())

            return ingredientsNames
