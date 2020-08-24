 # * author : Philippe Vo 
 # * date : Aug-22-2020 16:31:52
 
# * Imports
# 3rd Party Imports
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
# User Imports

# * Code
class ImageButton(QtWidgets.QAbstractButton):
    """
    class that allows an image to be clickable
    """
    def __init__(self, imgFilePath, width, height, objData, parent = None):
        """
        init. class

        Arguments
        ---------
        imgFilePath : str
            filepath to the image to be displayed
        width, height : int
            size of the image to be displayed
        objData : obj
            data storage of the obj that is represented by the image button
        """
        super(ImageButton, self).__init__(parent)

        # Sizes
        self.width = width
        self.height = height
        self.setFixedSize(self.width, self.height)

        # Pixmap
        pixmap = QtGui.QPixmap(imgFilePath)
        self.pixmap = pixmap.scaled(self.width, self.height)

        # Object Data
        self.objData = objData

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        # painter.drawPixmap(event.rect(), self.pixmap)

        # we want to draw rounded images
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        brush = QtGui.QBrush(self.pixmap)
        painter.setBrush(brush)
        painter.drawRoundedRect(event.rect(), 20, 20)

    def sizeHint(self):
        return self.pixmap.size()

    def set_pixmap(self, pixmapSet):
        # Pixmap
        self.pixmap = pixmapSet.scaled(self.width, self.height)
        self.update()

    # def resize(self, parentSize):
    #     """
    #     resize picture if the windows is resized
    #     """
    #     parentWidth = parentSize.width()
    #     parentHeight = parentSize.height()

    #     picResizeWidth = parentWidth / (COL_MAX_COUNT + 1) # maximum of collumn
    #     picResizeHeight = picResizeWidth * 1.25

    #     # setup style
    #     self.setFixedSize(picResizeWidth, picResizeHeight)


# class ImageButton(QtWidgets.QLabel):
#     """
#     class that allows an image to be clickable
#     """
#     def __init__(self, imgFilePath, width, height, objData, parent = None):
#         """
#         init. class

#         Arguments
#         ---------
#         imgFilePath : str
#             filepath to the image to be displayed
#         width, height : int
#             size of the image to be displayed
#         objData : obj
#             data storage of the obj that is represented by the image button
#         """
#         super(ImageButton, self).__init__(parent)

#         # Sizes
#         self.width = width
#         self.height = height

#         # Pixmap
#         pixmap = QtGui.QPixmap(imgFilePath)
#         self.pixmap = pixmap.scaled(self.width, self.height)
#         self.setPixmap(self.pixmap)

#         # self.setScaledContents(True)
#         # self.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

#         # Set Style
#         # self.setStyleSheet("{border-radius: 10px;}")
#         self.setStyleSheet("background-color:salmon; border-radius:50px")

#         # Object Data
#         self.objData = objData
