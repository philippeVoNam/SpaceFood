 # * author : Philippe Vo 
 # * date : Aug-23-2020 13:58:44
 
# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
# User Imports

# * Code
class RecipeBookView(QtWidgets.QWidget):
    """
    widget that displays ImageButtons in a grid format
    """
    def __init__(self):
        """
        init. class

        Arguments
        ---------
        imageButtons : [ImageButton]
            list of ImageButtons
        maxCol : int
            maximum number of images on a row displayed
        """
        super(RecipeBookView, self).__init__()

        # Init.

        # Setup the ui
        self.setup_ui()

        # Setup the image

    def setup_ui(self):
        """
        setup the ui
        """

