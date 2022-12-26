import requests
from bs4 import BeautifulSoup
from weather.models import Forecast

from datetime import datetime, timedelta


def _parse_data(city: str, day: str):
    """
        Parsing forecast from meteosite
    """
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
    """
        Update or create Forecast record
    """
    if not date:
        date = datetime.now()
    else:
        date = datetime.strptime(date, '%Y-%m-%d')

    for d in range(6):
        date_ = date + timedelta(days=d)
        date_ = date_.strftime('%Y-%m-%d')

        temp, description = _parse_data(city, date_)
        if not temp:
            continue
        try:
            forecast = Forecast.objects.get(date=date_)
        except Forecast.DoesNotExist:
            forecast = Forecast()
            forecast.date = date_
        forecast.time = datetime.now().strftime("%H:%M:%S")
        forecast.temperature = temp
        forecast.description = description
        forecast.save()
