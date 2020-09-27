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
class GridList(QtWidgets.QWidget):
    """
    grid layout where you can add widgets and have a scroll area
    """
    def __init__(self, colCountMax, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # setup ui
        self.layout = QtWidgets.QGridLayout()
        self.widgetsLayout = QtWidgets.QGridLayout()

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
        self.colCount = 0
        self.rowCount = 0
        self.colCountMax = colCountMax

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
            if self.colCount >= self.colCountMax:
                self.colCount = 0 # reset col count
                self.rowCount = self.rowCount + 1
                self.widgetsLayout.addWidget(widget, self.rowCount, self.colCount)

            else:
                self.widgetsLayout.addWidget(widget, self.rowCount, self.colCount)

            self.colCount = self.colCount + 1

            self.widgetBank[idName] = widget

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
