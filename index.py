from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import library
import sys

from PyQt5.uic import loadUiType

class MainApp(QMainWindow, library.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        self.groupBox.hide()

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_10.clicked.connect(self.Hide_Themes)
        self.darkBlueThemeButton.clicked.connect(self.Dark_Blue_Theme)
        self.darkOrangeThemeButton.clicked.connect(self.Dark_Orange_Theme)

    def Show_Themes(self):
        self.groupBox.show()

    def Hide_Themes(self):
        self.groupBox.hide()

    def Open_Day_To_Day_Tab(self):
        pass

    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
