 # * author : Philippe Vo 
 # * date : Aug-22-2020 16:31:38
 
# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
# User Imports

# * Code
class GridImagesView(QtWidgets.QWidget):
    """
    widget that displays ImageButtons in a grid format
    """
    def __init__(self, imageButtons, maxCol):
        """
        init. class

        Arguments
        ---------
        imageButtons : [ImageButton]
            list of ImageButtons
        maxCol : int
            maximum number of images on a row displayed
        """
        super(GridImagesView, self).__init__()

        # Init.
        self.imageButtons = imageButtons

        # Setup the ui
        self.setup_ui()

        # Setup the image
        self.set_image_buttons(self.imageButtons, maxCol)

    def setup_ui(self):
        """
        setup the ui
        """
        # Layout
        self.layout = QtWidgets.QGridLayout()
        self.gridLayout = QtWidgets.QGridLayout()

        # Widgets
        groupBox = QtWidgets.QGroupBox()
        groupBox.setLayout(self.gridLayout)

        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidget(groupBox)
        scrollArea.setWidgetResizable(True)

        self.layout.addWidget(scrollArea)

        # Setup
        self.setLayout(self.layout)

    def set_image_buttons(self, imageButtons, maxCol):
        """
        set the image buttons in a grid format
        """
        colCount = 0
        rowCount = 0
        for imageButton in imageButtons:
            if colCount >= maxCol:
                colCount = 0 # reset col count
                rowCount = rowCount + 1
                self.gridLayout.addWidget(imageButton, rowCount, colCount)

            else:
                self.gridLayout.addWidget(imageButton, rowCount, colCount)

            colCount = colCount + 1
