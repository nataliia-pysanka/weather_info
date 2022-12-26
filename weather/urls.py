from django.urls import path
from .views import ForecastListApiView, ScheduleApiView


urlpatterns = [
    path('api', ForecastListApiView.as_view()),
    path('schedule', ScheduleApiView.as_view())
]