from django.urls import path
from . import views

app_name = 'HR'
urlpatterns = [
  # ex: /HR/
  path('', views.index, name='index'),
]







# views.IndexView.as_view() instead of views.index?