from django.urls import path
from .views import InputBox
from . import views


urlpatterns = [
    path('', InputBox.as_view(), name='input box'),
]