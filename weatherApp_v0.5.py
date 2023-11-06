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

        self.weather_btn.clicked.connect(self.request_weather)

    def request_weather(self):
        area = self.input_areaBox.text() # 사용자가 입력한 지역이름을 가져오기
        weather_html = requests.get(f'https://search.naver.com/search.naver?&query={area}날씨')
        weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

        area_text = weather_soup.find('h2', {'class': 'title'}).text
        # 날씨를 조회하려는 지역주소 가져오기
        self.area_label.setText(area_text) # area_label 레이블 자리에 area_text를 출력
        today_temperature = weather_soup.find('div', {'class': 'temperature_text'}).text  # 현재온도
        today_temperature = today_temperature[6:11]
        self.temper_label.setText(today_temperature) # temper_label 레이블 자리에 today_temperature를 출력
        yesterday_weathertext = weather_soup.find('p', {'class': 'summary'}).text  # 어제온도와 현재온도의 비교
        yesterday_weathertext = yesterday_weathertext[:13].strip()
        self.yesterdayTemper_label.setText(yesterday_weathertext)
        sense_temperature = weather_soup.find('div', {'class': 'weather_info'}).find('dl', {'class': 'summary_list'}).find('dd', {'class': 'desc'}).text # 체감온도
        dust_info = weather_soup.select('ul.today_chart_list>li')
        dust1_info = dust_info[0].find('span', {'class': 'txt'}).text  # 미세먼지 정보
        dust2_info = dust_info[1].find('span', {'class': 'txt'}).text  # 초미세먼지 정보
        self.senseTemper_label.setText(sense_temperature) # 체감온도 출력
        self.dust1_label.setText(dust1_info) #미세먼지정보 출력
        self.dust2_label.setText(dust2_info) #초미세먼지정보 출력




if __name__== '__main__':
    app = QApplication(sys.argv)
    win = WeatherWin()
    win.show()
    sys.exit(app.exec_())

