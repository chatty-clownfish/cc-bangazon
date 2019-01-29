from django.urls import path
from . import views


app_name = 'HR'
urlpatterns = [
  # ex: /HR/
  path('', views.index, name='index'),
]

