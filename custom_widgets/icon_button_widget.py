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
class IconButton(QtWidgets.QPushButton):
    """
    image with an icon
    """
    clicked = QtCore.Signal()

    def __init__(self, imgPath, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pixmap = QtGui.QPixmap(imgPath)
        self.setIcon(QtGui.QIcon(pixmap))
        self.setIconSize(QtCore.QSize(100, 100))
        self.setMaximumSize(100,100)
        self.setObjectName("icon")
