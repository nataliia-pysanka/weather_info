from django.urls import path
from weather import views


urlpatterns = [
    path(r'', views.MainPage.as_view())
]