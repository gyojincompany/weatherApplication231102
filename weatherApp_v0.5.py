# weather Application v0.5

import sys
import requests
from bs4 import BeautifulSoup

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("ui/weatherAppUi.ui")[0]

class WeatherWin(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("오늘의 날씨")
        self.setWindowIcon(QIcon("img/weather_icon.png"))
        self.statusBar().showMessage("Weather Application Ver0.5")



if __name__== '__main__':
    app = QApplication(sys.argv)
    win = WeatherWin()
    win.show()
    sys.exit(app.exec_())

