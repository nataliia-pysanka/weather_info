import requests
from bs4 import BeautifulSoup
from weather.models import Forecast


def _parse_data(city: str):
    url = f'https://pogoda.meta.ua/ua/{city}'
    html_doc = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if html_doc.status_code == 200:
        soup = BeautifulSoup(html_doc.content, 'html.parser')
        temp = soup.find_all('div', class_='city__main-temp')[0].text
        description = soup.find_all('div',
                                    class_="city__main-description")[0].text
        return temp, description


def update_forecast(city: str = 'Kyiv'):
    temp, description = _parse_data(city)
    if temp is None:
        return
    try:
        new_forecast = Forecast()
        new_forecast.city = city
        new_forecast.temperature = temp
        new_forecast.description = description
        new_forecast.save()
    except Exception as e:
        print(e)
