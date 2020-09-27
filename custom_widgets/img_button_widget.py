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
class ImgButton(QtWidgets.QWidget):
    """
    image button that runs a function when clicked
    """
    clicked = QtCore.Signal()

    def __init__(self, text, imgPath, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # setup ui
        self.layout = QtWidgets.QVBoxLayout()

        self.setMaximumHeight(300)

        self.imgLabel = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(imgPath) # NOTE -> reading img is really slow here
        self.imgLabel.setPixmap(pixmap)
        self.imgLabel.setScaledContents(True);

        self.imgLabel.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.imgLabel.setMaximumSize(180,240)

        self.label = QtWidgets.QLabel(text)
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.layout.addWidget(self.imgLabel)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def mousePressEvent(self, env):
        """
        run a function when this widget is clicked
        """
        self.clicked.emit()
