# beautifulsoup4 설치
# requests 설치

import requests

from bs4 import BeautifulSoup

area = "한남동"

weather_html = requests.get(f'https://search.naver.com/search.naver?&query={area}날씨')
print(weather_html.text)

weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

today_temperature = weather_soup.find('div',{'class':'temperature_text'}).text # 현재온도
today_temperature = today_temperature[6:11]
print(today_temperature)

area_text = weather_soup.find('h2', {'class':'title'}).text #현재 날씨가 보여지고 있는 지역
print(area_text)

today_weathertext = weather_soup.find('span', {'class':'weather before_slash'}).text
print(today_weathertext)