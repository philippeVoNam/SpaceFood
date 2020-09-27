# * author : Philippe Vo
# * date : Aug-22-2020 00:52:03

# * Imports
# 3rd Party Imports
import sys
from PySide2 import QtWidgets
from PySide2 import QtGui
# User Imports
from ui.butler_view import ButlerView

# * Code
if __name__ == '__main__':

    # Init App
    app = QtWidgets.QApplication(sys.argv)

    # load font
    fontDb = QtGui.QFontDatabase()
    fontPixel = fontDb.addApplicationFont("resources/fonts/dogicapixel.ttf")

    # load stylesheet
    with open("resources/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    # Open MainWindow
    butlerView = ButlerView()
    butlerView.show()

    # Exit
    sys.exit(app.exec_())
