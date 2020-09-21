#!/usr/bin/env python3
#
# * author : Philippe Vo
# * date : Aug-22-2020 16:08:02

# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
# User Imports

# * Code
class FilterList(QtWidgets.QWidget):
    """
    list widget that has filter search
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # setup ui
        layout = QtWidgets.QVBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit()
        self.list_ = QtWidgets.QListWidget()

        self.lineEdit.textChanged.connect(self.text_changed)

        layout.addWidget(self.lineEdit)
        layout.addWidget(self.list_)

        self.setLayout(layout)

    def set_items(self, itemStrings):
        self.list_.addItems(itemStrings)
        self.itemStringsOG = itemStrings

    def text_changed(self):
        """
        function called whenever the text is changed in the search bar
        """
        itemsDisplay = []
        for item in self.itemStringsOG:
            if self.lineEdit.text().lower() in item.lower():
                itemsDisplay.append(item)

        self.list_.clear()
        self.list_.addItems(itemsDisplay)
