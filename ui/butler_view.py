#!/usr/bin/env python3
 # * author : Philippe Vo
 # * date : Aug-22-2020 16:08:02

# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
# User Imports
# from elements.dish import Dish
from elements.enums import DishCategories, Healthiness
from ui.dish_button import DishButton
# from custom_widgets.image_drag_drop import ImageDragDrop
# from custom_widgets.list_widget import FilterList
# from tools.ingredient_controller import IngredientController
# from resources.global_file_paths import ingredientBankFilePath
# from elements.ingredient import Ingredient
# from elements.component import Component
from tools.dish_controller import DishController
# from ui.ingredients_view import IngredientAddWidget
from custom_widgets.img_button_widget import ImgButton
from custom_widgets.grid_widget import GridList
from custom_widgets.icon_button_widget import IconButton
from resources.global_file_paths import iconsFolderPath
from ui.dish_create_view import DishCreateWindow
from ui.inventory_view import InventoryView
from tools.food_butler import FoodButler

# * Code
class ButlerView(QtWidgets.QMainWindow):
    """
    window where all the main operations will take place
    """
    def __init__(self):
        super(ButlerView, self).__init__()

        # inits
        self.dishController = DishController()

        # load in all the dishes in database
        self.dishes = self.dishController.load_all()

        # dish buttons
        self.dishButtons = []

        # setup ui
        self.setup_ui()
        self.setMinimumSize(700, 900)

    def setup_ui(self):
        """
        setup the ui
        """
        # Layout
        self.layout = QtWidgets.QGridLayout()

        # Widgets and Setup
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setObjectName("statusDish")

        self.categoryComboBox = QtWidgets.QComboBox()
        self.categoryComboBox.addItems([DishCategories.Breakfast.value, DishCategories.Lunch.value, DishCategories.Dinner.value, DishCategories.Snacks.value])
        self.categoryComboBox.currentTextChanged.connect(self.update_dish_grid)

        self.grid = GridList(colCountMax = 3)
        for dish in self.dishes:
            button = ImgButton(text = dish.name, imgPath = dish.dishImageFilePath)
            button.clicked.connect(dish.__str__)
            self.grid.add_widget(button, dish.name)

            dishButton = DishButton(dish, button)
            self.dishButtons.append(dishButton)

        self.scanDishesButton = IconButton(iconsFolderPath + "/food.png")
        self.fridgeButton = IconButton(iconsFolderPath + "/fridge.png")
        self.basketButton = IconButton(iconsFolderPath + "/basket.png")
        self.recipeButton = IconButton(iconsFolderPath + "/recipe.png")

        self.scanDishesButton.clicked.connect(self.scan_dishes)
        self.fridgeButton.clicked.connect(self.show_inventory)
        self.recipeButton.clicked.connect(self.show_recipe_book)

        self.layout.addWidget(self.categoryComboBox, 0, 1)
        self.layout.addWidget(self.grid, 1, 1, 4, 1)
        self.layout.addWidget(self.scanDishesButton, 0, 0)
        self.layout.addWidget(self.fridgeButton, 1, 0)
        self.layout.addWidget(self.basketButton, 2, 0)
        self.layout.addWidget(self.recipeButton, 3, 0)

        verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout.addItem(verticalSpacer, 4, 0)

        # Apply Layout
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.centralWidget().setLayout(self.layout)

        self.update_dish_grid()

    def update_dish_grid(self):
        category = self.categoryComboBox.currentText()

        for dishButton in self.dishButtons:
            if dishButton.dish.category.lower() != category.lower():
                dishButton.button.hide()

            else:
                dishButton.button.show()

    def scan_dishes(self):
        category = self.categoryComboBox.currentText()

        butler = FoodButler()
        butler.scan_available_dishes(category)

    def show_recipe_book(self):
        self.dishCreateWindow = DishCreateWindow()
        self.dishCreateWindow.show()

    def show_inventory(self):
        self.inventoryWindow = InventoryView()
        self.inventoryWindow.show()

    def set_red_status(self):
        """
        set the label to red text
        """
        style = """
        QStatusBar#statusDish {
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
        QStatusBar#statusDish {
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
        QStatusBar#statusDish {
            color: #eccc68;
            font-family:dogicapixel;
            font-size: 12px;
            font: bold;
        }
        """
        self.statusBar.setStyleSheet(style)
