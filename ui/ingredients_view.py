#!/usr/bin/env python3
 # * author : Philippe Vo
 # * date : Aug-22-2020 16:08:02

# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
from PySide2 import QtGui
# User Imports
from tools.ingredient_controller import IngredientController
from resources.global_file_paths import ingredientBankFilePath
from elements.ingredient import Ingredient
from elements.enums import SizeType

# * Code
class IngredientAddWidget(QtWidgets.QWidget):
    """
    widget to allow the user to add ingredients and save them locally
    """
    def __init__(self):
        super(IngredientAddWidget, self).__init__()

        self.setup_ui()

        # set the ingredients list
        self.ingredientController = IngredientController(ingredientBankFilePath)

    def setup_ui(self):
        """
        setup the ui
        """
        # Layout
        self.layout = QtWidgets.QGridLayout()

        # Widgets and Setup
        self.ingredientNameLineEdit = QtWidgets.QLineEdit()
        self.ingredientNameLineEdit.setPlaceholderText("Ingredient Name")

        self.caloriesSpinBox = QtWidgets.QSpinBox()
        self.caloriesSpinBox.setRange(0, 1000)
        self.caloriesSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        self.addIngredientButton = QtWidgets.QPushButton("Add")
        self.addIngredientButton.clicked.connect(self.add_ingredient)

        self.addStatusLabel = QtWidgets.QLabel("status")

        self.layout.addWidget(self.ingredientNameLineEdit, 0, 0)
        self.layout.addWidget(self.caloriesSpinBox, 0, 1)
        self.layout.addWidget(self.addIngredientButton, 0, 2)
        self.layout.addWidget(self.addStatusLabel, 1, 0)

        # setup style
        style = """
        QWidget#IngredientAddBox {
            background-color: #1C1E26;
        }
        """
        self.setObjectName("IngredientAddBox")
        self.setStyleSheet(style)

        style = """
        QLabel#statusLabel {
            border-radius: 0px;
            color: white;
            font-family:dogicapixel;
            font-size: 12px;
            qproperty-alignment: AlignLeft;
        }
        """
        self.addStatusLabel.setObjectName("statusLabel")
        self.addStatusLabel.setStyleSheet(style)

        # Apply Layout
        self.setLayout(self.layout)

    def add_ingredient(self):
        """
        add ingredient to ingredient bank
        """
        ingredientName = self.ingredientNameLineEdit.text()
        caloriesper100 = self.caloriesSpinBox.value()

        if not ingredientName or caloriesper100 < 0:
            self.set_red_status()
            print("invalid ingredient")
            self.addStatusLabel.setText("invalid ingredient (ó_ò｡)")

        else:
            ingredient = Ingredient(ingredientName, caloriesper100, SizeType.Per100g.value)

            result = self.ingredientController.append(ingredient)

            if result:
                self.set_green_status()
                print("ingredient added !")
                self.addStatusLabel.setText("ingredient added o(^▽^)o")

            else:
                self.set_yellow_status()
                self.addStatusLabel.setText("ingredient already exists (^o^)v")

    def set_red_status(self):
        """
        set the label to red text
        """
        style = """
        QLabel#statusLabel {
            border-radius: 0px;
            color: #ff6b81;
            font-family:dogicapixel;
            font-size: 12px;
            qproperty-alignment: AlignLeft;
            font: bold;
        }
        """
        self.addStatusLabel.setStyleSheet(style)

    def set_green_status(self):
        """
        set the label to red text
        """
        style = """
        QLabel#statusLabel {
            border-radius: 0px;
            color: #7bed9f;
            font-family:dogicapixel;
            font-size: 12px;
            qproperty-alignment: AlignLeft;
            font: bold;
        }
        """
        self.addStatusLabel.setStyleSheet(style)

    def set_yellow_status(self):
        """
        set the label to red text
        """
        style = """
        QLabel#statusLabel {
            border-radius: 0px;
            color: #eccc68;
            font-family:dogicapixel;
            font-size: 12px;
            qproperty-alignment: AlignLeft;
            font: bold;
        }
        """
        self.addStatusLabel.setStyleSheet(style)
