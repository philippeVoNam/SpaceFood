 # * author : Philippe Vo 
 # * date : Aug-23-2020 19:15:00
 
# * Imports
# 3rd Party Imports
# User Imports

# * Code
class DishButton:
    """
    widget that displays the recipe of a dish
    """
    def __init__(self, dish, button):
        """
        init. class

        Arguments
        ---------
        dish : [Dish]
            recipe with all the information about it
        mode : str
            editable or just for show
        """
        # Init.
        self.dish = dish
        self.button = button
