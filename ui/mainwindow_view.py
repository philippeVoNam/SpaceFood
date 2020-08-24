 # * author : Philippe Vo 
 # * date : Aug-22-2020 16:08:02
 
# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
from PySide2 import QtGui
# User Imports
from ui.grid_images_view import GridImagesView
from ui.image_button import ImageButton
from ui.dish_view import DishView, AddDishView
from elements.dish import Dish
from elements.enums import DishModes

# * Code
class MainWindow(QtWidgets.QMainWindow):
    """
    class that describes the main menu of the application -> starting window of the app
    """
    def __init__(self):
        """
        init. class
        """
        super(MainWindow, self).__init__()

        # Setup the ui
        # self.setup_ui()
        self.test_setup_ui()

    def setup_ui(self):
        """
        setup the ui
        """
        # Layout
        mainLayout = QtWidgets.QGridLayout()
       
        # Widgets

        # Setup

    def test_setup_ui(self):
        tabWidget = QtWidgets.QTabWidget()
        tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        mainLayout = QtWidgets.QGridLayout()

        dishes = []
        addDishView = AddDishView()
        dishes.append(addDishView)
        for i in range(20):
            dish = Dish("", "", "" ,"", "", "", "img.jpg")
            dishView = DishView(dish, DishModes.Editable)
            dishes.append(dishView)

        gridImage = GridImagesView(dishes, 5)
        gridImage1 = GridImagesView(dishes, 5)

        index1 = tabWidget.addTab(gridImage, "BreakFast")
        index2 = tabWidget.addTab(gridImage1, "Lunch")

        tabWidget.setTabIcon(index2, QtGui.QIcon('resources/icons/lunch.png'))
        tabWidget.setTabPosition(QtWidgets.QTabWidget.West)

        mainLayout.addWidget(tabWidget)

        self.setCentralWidget(QtWidgets.QWidget(self))
        self.centralWidget().setLayout(mainLayout)
