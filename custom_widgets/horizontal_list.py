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
class HorizontalList(QtWidgets.QWidget):
    """
    horizontal layout where you can add widgets and have a scroll area
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # setup ui
        self.layout = QtWidgets.QHBoxLayout()
        self.widgetsLayout = QtWidgets.QHBoxLayout()

        groupBox = QtWidgets.QGroupBox()
        groupBox.setLayout(self.widgetsLayout)
        groupBox.setFlat(True)
        groupBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidget(groupBox)
        self.scroll.setWidgetResizable(True)
        self.scroll.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)

        # init
        self.widgetBank = {}

    def add_widget(self, widget, idName):
        """
        add widget to the layout
        need idName as well so that we can access from outside

        Arguments
        ---------
        widget : QtWidgets
            widget
        idName : str
            name id
        """
        # verify if idName already exists
        keyList = list(self.widgetBank.keys())
        if idName in keyList:
            print("idName : " + idName + " already exists")
       
        else:
            self.widgetsLayout.addWidget(widget)
            self.widgetBank[idName] = widget

    def widget_in_grid(self, idName):
        # verify if idName  exists
        keyList = list(self.widgetBank.keys())
        if idName not in keyList:
            return False

        else:
            return True

    def remove_widget(self, idName):
        # verify if idName  exists
        keyList = list(self.widgetBank.keys())
        if idName not in keyList:
            print("idName : " + idName + " does not exists")

        else:
            self.widgetBank[idName].setParent(None)
            del self.widgetBank[idName] # remove the button

    def hide_widget(self, idName):
        # verify if idName  exists
        keyList = list(self.widgetBank.keys())
        if idName not in keyList:
            print("idName : " + idName + " does not exists")

        else:
            self.widgetBank[idName].hide()

    def show_widget(self, idName):
        # verify if idName  exists
        keyList = list(self.widgetBank.keys())
        if idName not in keyList:
            print("idName : " + idName + " does not exists")

        else:
            self.widgetBank[idName].show()

    def clear(self):
        # verify if idName  exists
        keyList = list(self.widgetBank.keys())

        for idName in keyList:
            self.widgetBank[idName].setParent(None)
            del self.widgetBank[idName] # remove the button
