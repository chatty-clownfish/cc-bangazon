from django.urls import path
from . import views


app_name = 'HR'
urlpatterns = [
  # 1. url 2. invoking method 3. nickname for url
  # ex: /HR/
  path('', views.index, name='index'),
  # employees list
  path('employees/', views.employeeList , name = 'employees'),
  # add employee
  path('addemployee/', views.addEmployee, name='addemployee'),
  # edit employee
  path('editemployee/<int:employee_id>/', views.editEmployee, name='editemployee'),
  # department index
  path('departments/', views.departmentIndex, name='departments'),
  # department details
  path('departments/<int:dept_id>/', views.dept_details, name='deptDetails'),
  path('training/', views.trainingList, name='trainings'),
  path('addTraining/', views.add_training_program, name='add'),
  path('training/<int:id>/', views.trainingDetails, name='trainingDetail'),
  

]

