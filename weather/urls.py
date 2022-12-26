from django.urls import path
from .views import ForecastListApiView, MainPage, ScheduleApiView


urlpatterns = [
    path('', MainPage.as_view()),
    path('api', ForecastListApiView.as_view()),
    path('schedule', ScheduleApiView.as_view())
]