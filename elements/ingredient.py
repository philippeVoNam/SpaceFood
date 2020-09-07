 # * author : Philippe Vo 
 # * date : Sep-05-2020 15:31:29
 
# * Imports
# 3rd Party Imports
from elements.enums import SizeType
# User Imports

# * Code
class Ingredient():
    """
    class that represents ingredients
    """
    def __init__(self, name, calories, type_):
        """
        init.

        Arguments
        ---------
        name : str
            name of the dish
        calories : int
            how much calories does it have per unit
        type_ : enums.SizeType
            either unit "1" or per100g "100g / calories"
        """
        self.name = name.lower()
        self.calories = calories
        self.type_ = type_
        self.caloriesMultiplier = self.calories_multiplier(calories, type_)

    def calories_multiplier(self, calories, type_):
        """
        depending on the type, give a different calories calculator function -> this assumes that the calories is given by either unit or "100 grams"
        """
        if type_ == SizeType.Unit.value:
            return calories / 1

        elif type_ == SizeType.Per100g.value:
            return calories / 100

    def pickle_it(self):
        """
        returns the dict representation of this object
        """
        data = {
            "name" : self.name,
            "calories" : self.calories,
            "type_" : self.type_
        }
        return data
