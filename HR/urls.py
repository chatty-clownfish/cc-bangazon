from django.urls import path
from . import views


app_name = 'HR'
urlpatterns = [
  # ex: /HR/
  path('', views.index, name='index'),
  path('departments/', views.departmentIndex, name='departments'),
  path('departments/<int:dept_id>/', views.details, name='deptDetails'),
  path('employees/', views.employeeList , name = 'employees'),
  path('training/', views.trainingList, name='trainings'),
  path('addTraining/', views.addTraining, name='add'),

]

