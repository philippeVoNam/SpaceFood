 # * author : Philippe Vo 
 # * date : Sep-06-2020 20:56:35
 
# * Imports
# 3rd Party Imports
import yaml
from pathlib import Path
# User Imports

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

            if data["name"].lower() not in ingredientsNames:
                loadedData.append(data)

            else:
                print("ingredient already in")

        if loadedData:
            with open(self.filePath,'w') as yamlfile:
                yaml.safe_dump(loadedData, yamlfile) # Also note the safe_dump

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
