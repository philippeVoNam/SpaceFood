#!/usr/bin/env python3
 # * author : Philippe Vo
 # * date : Aug-22-2020 16:08:02

# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
from PySide2 import QtGui
# User Imports
from elements.dish import Dish
from elements.enums import DishCategories, Healthiness
from custom_widgets.image_drag_drop import ImageDragDrop
from custom_widgets.list_widget import FilterList
from tools.ingredient_controller import IngredientController
from resources.global_file_paths import ingredientBankFilePath
from elements.ingredient import Ingredient
from elements.component import Component
from tools.dish_controller import DishController

# * Code
class DishCreateWindow(QtWidgets.QMainWindow):
    """
    window to allow the user to create dishes and save them locally
    """
    def __init__(self):
        super(DishCreateWindow, self).__init__()

        self.setup_ui()

        # set the ingredients list
        self.ingredientController = IngredientController(ingredientBankFilePath)
        ingredientList = self.ingredientController.get_names()
        self.ingredientList.set_items(ingredientList)

    def setup_ui(self):
        """
        setup the ui
        """
        # Layout
        self.layout = QtWidgets.QGridLayout()

        # Widgets and Setup
        self.dishNameLineEdit = QtWidgets.QLineEdit()
        self.dishNameLineEdit.setPlaceholderText("Dish Name")

        self.categoryComboBox = QtWidgets.QComboBox()
        self.categoryComboBox.addItems([DishCategories.Breakfast.value, DishCategories.Lunch.value, DishCategories.Dinner.value, DishCategories.Snacks.value])

        self.healthComboBox = QtWidgets.QComboBox()
        self.healthComboBox.addItems([Healthiness.Healthy.value, Healthiness.Neutral.value, Healthiness.Fatenning.value])

        self.descriptionTextBox = QtWidgets.QPlainTextEdit()
        self.descriptionTextBox.setPlaceholderText("enter a short description")

        self.ingredientList = FilterList()
        self.componentInputTextBox = QtWidgets.QPlainTextEdit()
        self.ingredientList.list_.itemClicked.connect(self.ingredient_clicked)

        self.imageDragDrop = ImageDragDrop()

        self.createDishButton = QtWidgets.QPushButton("Create Dish")
        self.createDishButton.clicked.connect(self.create_dish)

        self.layout.addWidget(self.dishNameLineEdit, 0, 0, 1, 2)
        self.layout.addWidget(self.categoryComboBox, 1, 0, 1, 2)
        self.layout.addWidget(self.healthComboBox, 2, 0, 1, 2)
        self.layout.addWidget(self.descriptionTextBox, 3, 0, 1, 2)
        self.layout.addWidget(self.ingredientList, 4, 0)
        self.layout.addWidget(self.componentInputTextBox, 4, 1)
        self.layout.addWidget(self.imageDragDrop, 5, 0, 1, 2)
        self.layout.addWidget(self.createDishButton, 6, 0, 1, 2)

        # Apply Layout
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.centralWidget().setLayout(self.layout)

    def ingredient_clicked(self, item):
        """
        insert ingredient into component text box
        """
        self.componentInputTextBox.appendPlainText(item.text())

    def create_dish(self):

        # gather all the data
        name = self.dishNameLineEdit.text()

        category = self.categoryComboBox.currentText()

        healthiness = self.healthComboBox.currentText()

        description = self.descriptionTextBox.toPlainText()

        componentText = self.componentInputTextBox.toPlainText()
        components = self.load_from_text(componentText) # read the component Text box and returns the components

        try:
            dishImgFilePath = self.imageDragDrop.get_image_filePath()

        except Exception as e:
            print("missing image")
            dishImgFilePath = "default.jpg"

        # verify the data
        if not name or not category or not healthiness or not description or len(components) == 0:
            print("invalid dish")

        else:
            # create dish
            dish = Dish(name, category, description.strip(), components, healthiness, dishImgFilePath)
            controllerDish = DishController()
            controllerDish.create(dish)
   
    def load_from_text(self, text):
        """
        load all the components to see what we have from raw text
        """
        data = text.splitlines()

        components = []
        for componentData in data:
            componentData = componentData.split(",")
            ingredientName = componentData[0]
            ingredient = self.ingredientController.read(ingredientName)
            quantity = int(componentData[1])

            component = Component(ingredient, quantity)
            components.append(component)

        return components
