# * author : Philippe Vo
# * date : Aug-22-2020 00:52:03

# * Imports
# 3rd Party Imports
import sys
from PySide2 import QtWidgets
# User Imports
from ui.mainwindow_view import MainWindow

# * Code
if __name__ == '__main__':

    # Init App
    app = QtWidgets.QApplication(sys.argv)

    # Open MainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    # Exit
    sys.exit(app.exec_())
