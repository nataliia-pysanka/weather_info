from django.urls import path
from .views import ForecastListApiView


urlpatterns = [
    path('api', ForecastListApiView.as_view()),
]