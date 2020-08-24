 # * author : Philippe Vo 
 # * date : Aug-23-2020 19:15:00
 
# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
from pathlib import Path
# User Imports
from elements.enums import DishModes
from ui.image_button import ImageButton
from resources.global_file_paths import iconsFolderPath

# * Code
class DishView(QtWidgets.QWidget):
    """
    widget that displays the recipe of a dish
    """
    def __init__(self, dish, mode):
        """
        init. class

        Arguments
        ---------
        dish : [Dish]
            recipe with all the information about it
        mode : str
            editable or just for show
        """
        super(DishView, self).__init__()

        # Init.
        self.dish = dish
        self.mode = mode

        # Setup the ui
        self.setup_ui()

        # Setup the image

    def setup_ui(self):
        """
        setup the ui
        """
        # layout
        layout = QtWidgets.QGridLayout()

        # widgets
        width = 250
        height = 400
        imgButton = ImageButton(self.dish.dishImageFilePath, width, height, self.dish)

        if self.mode == DishModes.Editable:
            editIconFilePath = str(Path(iconsFolderPath) / "edit.png")
            editButton = ImageButton(editIconFilePath, 30, 30, "")

            binIconFilePath = str(Path(iconsFolderPath) / "bin.png")
            deleteButton = ImageButton(binIconFilePath, 30, 30, "")

            layout.addWidget(imgButton, 0, 1)
            layout.addWidget(editButton, 1, 0)
            layout.addWidget(deleteButton, 1, 2)

        else:
            layout.addWidget(imgButton, 0, 0)

        # setup
        self.setLayout(layout)

class AddDishView(QtWidgets.QWidget):
    """
    widget that displays button to add new dish
    """
    def __init__(self):
        """
        init. class
        """
        super(AddDishView, self).__init__()

        # Init.

        # Setup the ui
        self.setup_ui()

        # Setup the image

    def setup_ui(self):
        """
        setup the ui
        """
        # layout
        layout = QtWidgets.QGridLayout()

        # widgets
        width = 250
        height = 400
        addImageFilePath = str(Path(iconsFolderPath) / "add.png")
        imgButton = ImageButton(addImageFilePath, width, height, "")

        layout.addWidget(imgButton, 0, 0)

        # setup
        self.setLayout(layout)
