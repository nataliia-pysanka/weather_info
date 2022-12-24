import requests
from bs4 import BeautifulSoup
from weather.models import Forecast

from datetime import datetime, timedelta


def _parse_data(city: str, day: str):
    url = f'https://pogoda.meta.ua/ua/{city}/{day}/ajax/'
    html_doc = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if html_doc.status_code == 200:
        soup = BeautifulSoup(html_doc.content, 'html.parser')

        temp = str(soup.find_all('div', class_='city__main-temp')[0].text)
        description = str(soup.find_all('div',
                                    class_="city__main-description")[0].text)
        return temp, description
    return None, None


def update_forecast(city: str, date: str = None):
    if not date:
        date = datetime.now()
    else:
        date = datetime.strptime(date, '%Y-%m-%d')

    for d in range(5):
        date_ = date + timedelta(days=d)
        date_ = date_.strftime('%Y-%m-%d')

        temp, description = _parse_data(city, date_)

        try:
            new_forecast = Forecast()
            new_forecast.date = date_
            new_forecast.temperature = temp
            new_forecast.description = description
            new_forecast.save()
        except Exception as e:
            print(e)
