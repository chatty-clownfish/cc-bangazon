from django.urls import path
from . import views


app_name = 'HR'
urlpatterns = [
  # ex: /HR/
  path('', views.index, name='index'),
  path('employees/', views.employeeList , name = 'employees'),
  path('training/', views.trainingList, name='trainings'),
  path('addTraining/', views.addTraining, name='add'),
]

