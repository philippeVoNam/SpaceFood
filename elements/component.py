 # * author : Philippe Vo 
 # * date : Sep-07-2020 00:09:21
 
# * Imports
# 3rd Party Imports
# User Imports

# * Code
class Component():
    """
    class to group Ingredient and quantity
    """
    def __init__(self, ingredient, quantity):
        """ init. """
        # inits.
        self.ingredient = ingredient
        self.quantity = quantity

    def pickle_it(self):
        """
        returns the dict representation of this object
        """
        data = {}
        ingredientData = self.ingredient.pickle_it() # turn ingredient to a dict representation
        quantityData = self.quantity

        data["ingredient"] = ingredientData
        data["quantity"] = quantityData

        return data

    def calories_cal(self):
        """
        calculate the number of calories in the component
        """
        calories = self.ingredient.caloriesMultiplier * self.quantity

        return calories
