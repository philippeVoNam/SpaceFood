 # * author : Philippe Vo 
 # * date : Sep-06-2020 20:56:35
 
# * Imports
# 3rd Party Imports
import yaml
from pathlib import Path
# User Imports
from elements.ingredient import Ingredient
from elements.component import Component

# * Code
class InventoryController():
    """
    class used to control the elements.Components
    """
    def __init__(self, filePath):
        """ init. """
        # inits.
        self.filePath = Path(filePath)

    def append(self, component):
        """
        add ingredient to Inventory Bank

        Arguments
        ---------
        component : elements.Component
        """
        with open(self.filePath, 'r') as yamlfile:
            loadedData = yaml.safe_load(yamlfile) # Note the safe_load

            ingredientsNames = []
            for componentLoadedData in loadedData:
                ingredientsNames.append(componentLoadedData["ingredient"]["name"].lower())

            data = component.pickle_it()

            if component.ingredient.name.lower() not in ingredientsNames:
                loadedData.append(data)

            else:
                print("ingredient already in")

        if loadedData:
            with open(self.filePath,'w') as yamlfile:
                yaml.safe_dump(loadedData, yamlfile) # Also note the safe_dump

    def remove(self, ingredientName):
        """
        remove ingredient to Inventory Bank

        Arguments
        ---------
        ingredientName : str
        """
        with open(self.filePath, 'r') as yamlfile:
            loadedData = yaml.safe_load(yamlfile) # Note the safe_load

            ingredientsNames = []
            for componentLoadedData in loadedData:
                ingredientsNames.append(componentLoadedData["ingredient"]["name"].lower())

            if ingredientName.lower() in ingredientsNames:
                for componentLoadedData in loadedData:
                    if componentLoadedData["ingredient"]["name"].lower() == ingredientName.lower():
                        loadedData.remove(componentLoadedData)

            else:
                print("ingredient not in bank")

        if loadedData:
            with open(self.filePath,'w') as yamlfile:
                yaml.safe_dump(loadedData, yamlfile) # Also note the safe_dump

    def edit(self, editedComponent):
        """
        edit ingredient to Ingredients Bank

        Arguments
        ---------
        ingredient : elements.Ingredient
        """
        # remove the current ingredient
        self.remove(editedComponent.ingredient.name)

        # append the edited ingredient
        self.append(editedComponent)

    def load(self):
        """
        load all the components to see what we have
        """
        with open(self.filePath, 'r') as yamlfile:
            loadedData = yaml.safe_load(yamlfile) # Note the safe_load

            components = []
            for component in loadedData:
                ingredientCp = component["ingredient"]
                ingredient = Ingredient(ingredientCp["name"], int(ingredientCp["calories"]), ingredientCp["type_"])
                quantity = int(component["quantity"])

                component = Component(ingredient, quantity)
                components.append(component)

            return components

    def load_from_text(self, text):
        """
        load all the components to see what we have from raw text
        """
        data = text.splitlines()
        print(data)
        # components = []
        # for component in loadedData:
        #     ingredientCp = component["ingredient"]
        #     ingredient = Ingredient(ingredientCp["name"], int(ingredientCp["calories"]), ingredientCp["type_"])
        #     quantity = int(component["quantity"])

        #     component = Component(ingredient, quantity)
        #     components.append(component)

        # return components
