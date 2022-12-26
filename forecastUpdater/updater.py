from apscheduler.schedulers.background import BackgroundScheduler
from forecastUpdater import forecastScrapper


scheduler = BackgroundScheduler()
data = {'trigger': 'cron', 'args': ['Kyivska/Kyivskiy/Kyiv'],
        'id': 'forecast_app', 'day_of_week': '*', 'hour': 9}


def start():
    """
        Starting schedule for task
    """
    scheduler.add_job(forecastScrapper.update_forecast, **data)
    scheduler.start()


def reschedule(kwargs):
    """
        Changing time (hour) for schedule
    """
    scheduler.reschedule_job(job_id="forecast_app", **kwargs)
