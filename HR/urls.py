from django.urls import path
from . import views


app_name = 'HR'
urlpatterns = [
  # ex: /HR/
  path('', views.index, name='index'),
  # adds a new artist via form
  path('addemployee/', views.addEmployee, name='addemployee'),


  # department index
  path('departments/', views.departmentIndex, name='departments'),
  # department details
  path('departments/<int:dept_id>/', views.details, name='deptDetails')

  path('employees/', views.employeeList , name = 'employees'),
  
  path('training/', views.trainingList, name='trainings'),
  path('addTraining/', views.addTraining, name='add'),

]

