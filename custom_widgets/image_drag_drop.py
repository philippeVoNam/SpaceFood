#!/usr/bin/env python3
 # * author : Philippe Vo
 # * date : Aug-22-2020 16:08:02

# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
# User Imports

# * Code
class ImageLabel(QtWidgets.QLabel):
    """
    label that can contain an image
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # style
        styleSheet = """
        QLabel
        {
            border: 4px dashed #5352ed;
            min-height: 200;
            min-width: 200;
            max-height: 300;
            qproperty-alignment: AlignCenter;
        }
        """
        self.setStyleSheet(styleSheet)

        self.setScaledContents(True)

        self.setText("Drop Image Here")

    def setPixmap(self, pixMap):
        super().setPixmap(pixMap)

class ImageDragDrop(QtWidgets.QWidget):
    """
    area to drag and drop image
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # setup ui
        mainLayout = QtWidgets.QVBoxLayout()

        self.imageViewer = ImageLabel()

        mainLayout.addWidget(self.imageViewer)

        self.setLayout(mainLayout)

        # setup drag and drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()

        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()

        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:

            event.setDropAction(QtCore.Qt.CopyAction)

            self.imgFilePath= event.mimeData().urls()[0].toLocalFile()
            self.set_image(self.imgFilePath)

            event.accept()

        else:
            event.ignore()

    def set_image(self, filePath):
        self.imageViewer.setPixmap(QtGui.QPixmap(filePath))

    def get_image_filePath(self):
        return self.imgFilePath
