#!/usr/bin/env python3
 # * author : Philippe Vo
 # * date : Aug-22-2020 16:08:02

# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
from PySide2 import QtGui
# User Imports
# from elements.dish import Dish
# from elements.enums import DishCategories, Healthiness
# from custom_widgets.image_drag_drop import ImageDragDrop
from custom_widgets.list_widget import FilterList
from tools.inventory_controller import InventoryController
# from tools.ingredient_controller import IngredientController
# from resources.global_file_paths import ingredientBankFilePath
# from elements.ingredient import Ingredient
from elements.component import Component
# from tools.dish_controller import DishController
from ui.ingredients_view import IngredientAddWidget
# from custom_widgets.img_button_widget import ImgButton
# from custom_widgets.grid_widget import GridList
from ui.inventory_add_view import InventoryAddWidget
from tools.ingredient_controller import IngredientController
from resources.global_file_paths import ingredientBankFilePath, inventoryFilePath

# * Code
class InventoryView(QtWidgets.QMainWindow):
    """
    window to allow the user to add/edit their inventory
    """
    def __init__(self):
        super(InventoryView, self).__init__()

        self.setup_ui()
        self.setMinimumSize(700, 900)

        # set the ingredients list
        self.ingredientController = IngredientController(ingredientBankFilePath)
        ingredientList = self.ingredientController.get_names()
        self.ingredientList.set_items(ingredientList)

        self.componentController = InventoryController(inventoryFilePath)
        components = self.componentController.load()

        componentsData = []
        for component in components:
            componentData = component.ingredient.name + " - " + str(component.quantity) + "g"
            componentsData.append(componentData)

        self.inventoryList.set_items(componentsData)

    def setup_ui(self):
        """
        setup the ui
        """
        # Layout
        self.layout = QtWidgets.QGridLayout()

        # Widgets and Setup
        self.inventoryAddWidget = InventoryAddWidget()
        self.ingredientAddWidget = IngredientAddWidget()

        self.inventoryList = FilterList()
        self.inventoryList.list_.itemClicked.connect(self.edit_component)

        self.ingredientList = FilterList()

        self.refreshButton = QtWidgets.QPushButton("Refresh")
        self.inventoryList.layout.addWidget(self.refreshButton)
        self.refreshButton.clicked.connect(self.refresh_inventory)

        self.refreshButton = QtWidgets.QPushButton("Refresh")
        self.ingredientList.layout.addWidget(self.refreshButton)
        self.refreshButton.clicked.connect(self.refresh_ingredients_bank)

        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setObjectName("statusInventory")

        self.layout.addWidget(self.ingredientAddWidget, 0, 0)
        self.layout.addWidget(self.inventoryAddWidget, 0, 1)
        self.layout.addWidget(self.ingredientList, 1, 0)
        self.layout.addWidget(self.inventoryList, 1, 1)

        # Apply Layout
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.centralWidget().setLayout(self.layout)

    def edit_component(self, item):
        data = item.text().split("-")
        ingredientName = data[0].strip()

        quantity ,ok = QtWidgets.QInputDialog.getInt(self,"Inventory Edit","quantity")

        ingredient = self.ingredientController.read(ingredientName)
        editedComponent = Component(ingredient, quantity)

        self.componentController.edit(editedComponent)

    def refresh_ingredients_bank(self):
        self.ingredientList.list_.clear()

        ingredientList = self.ingredientController.get_names()
        self.ingredientList.set_items(ingredientList)

    def refresh_inventory(self):
        self.inventoryList.list_.clear()

        components = self.componentController.load()

        componentsData = []
        for component in components:
            componentData = component.ingredient.name + " - " + str(component.quantity) + "g"
            componentsData.append(componentData)

        self.inventoryList.set_items(componentsData)

    def set_red_status(self):
        """
        set the label to red text
        """
        style = """
        QStatusBar#statusInventory {
            color: #ff6b81;
            font-family:dogicapixel;
            font-size: 12px;
            font: bold;
        }
        """
        self.statusBar.setStyleSheet(style)

    def set_green_status(self):
        """
        set the label to red text
        """
        style = """
        QStatusBar#statusInventory {
            color: #7bed9f;
            font-family:dogicapixel;
            font-size: 12px;
            font: bold;
        }
        """
        self.statusBar.setStyleSheet(style)

    def set_yellow_status(self):
        """
        set the label to red text
        """
        style = """
        QStatusBar#statusInventory {
            color: #eccc68;
            font-family:dogicapixel;
            font-size: 12px;
            font: bold;
        }
        """
        self.statusBar.setStyleSheet(style)
