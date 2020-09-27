#!/usr/bin/env python3
 # * author : Philippe Vo
 # * date : Aug-22-2020 16:08:02

# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
# User Imports
from tools.ingredient_controller import IngredientController
from tools.inventory_controller import InventoryController
from resources.global_file_paths import ingredientBankFilePath, inventoryFilePath
from elements.ingredient import Ingredient
from elements.enums import SizeType
from elements.component import Component

# * Code
class InventoryAddWidget(QtWidgets.QWidget):
    """
    widget to allow the user to add component and save them locally
    """
    def __init__(self):
        super(InventoryAddWidget, self).__init__()

        # set the ingredients list
        self.ingredientController = IngredientController(ingredientBankFilePath)
        self.inventoryController = InventoryController(inventoryFilePath)
        self.ingredientList = self.ingredientController.get_names()

        # setup ui
        self.setup_ui()

    def setup_ui(self):
        """
        setup the ui
        """
        # Layout
        self.layout = QtWidgets.QGridLayout()

        # Widgets and Setup
        self.ingredientNameLineEdit = QtWidgets.QLineEdit()
        self.ingredientNameLineEdit.setPlaceholderText("Ingredient Name")

        # adding the auto complete
        self.completer = QtWidgets.QCompleter()
        self.ingredientNameLineEdit.setCompleter(self.completer)
        self.model = QtCore.QStringListModel()
        self.completer.setModel(self.model)
        self.model.setStringList(self.ingredientList)
        self.completer.setCompletionMode(QtWidgets.QCompleter.InlineCompletion)

        self.quantitySpinBox = QtWidgets.QSpinBox()
        self.quantitySpinBox.setRange(0, 1000)
        self.quantitySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        self.quantityLabel = QtWidgets.QLabel("grams")

        self.addComponentButton = QtWidgets.QPushButton("Add")
        self.addComponentButton.clicked.connect(self.add_component)

        self.addStatusLabel = QtWidgets.QLabel("status")

        self.layout.addWidget(self.ingredientNameLineEdit, 0, 0)
        self.layout.addWidget(self.quantitySpinBox, 0, 1)
        self.layout.addWidget(self.quantityLabel, 0, 2)
        self.layout.addWidget(self.addComponentButton, 0, 3)
        self.layout.addWidget(self.addStatusLabel, 1, 0)

        # setup style
        style = """
        QWidget#InventoryAddBox {
            background-color: #1C1E26;
        }
        """
        self.setObjectName("InventoryAddBox")
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

    def add_component(self):
        """
        add component to inventory bank
        """
        ingredientName = self.ingredientNameLineEdit.text()
        quantity = self.quantitySpinBox.value()

        if not ingredientName or quantity < 0:
            self.set_red_status()
            print("invalid component")
            self.addStatusLabel.setText("invalid component (ó_ò｡)")

        else:
            ingredient = self.ingredientController.read(ingredientName)

            if ingredient != None:
                component = Component(ingredient, quantity)

                result = self.inventoryController.append(component)

                if result:
                    self.set_green_status()
                    print("component added !")
                    self.addStatusLabel.setText("component added o(^▽^)o")

                else:
                    self.set_yellow_status()
                    self.addStatusLabel.setText("component already exists (^o^)v")

            else:
                self.set_red_status()
                print("invalid component")
                self.addStatusLabel.setText("invalid component (ó_ò｡)")

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
