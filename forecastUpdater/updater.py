from apscheduler.schedulers.background import BackgroundScheduler
from forecastUpdater import forecastScrapper


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(forecastScrapper.update_forecast, 'cron',
                      ['Kyivska/Kyivskiy/Kyiv'],
                      day_of_week='*', second=0)
    scheduler.start()
