from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from forecastUpdater import forecastScrapper


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(forecastScrapper.update_forecast,
                      'cron', day_of_week='*', minute=10)
    scheduler.start()
