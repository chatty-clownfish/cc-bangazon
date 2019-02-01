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
  # route to edit employee
  path('editedemployee/<int:employee_id>/', views.editEmployee, name='editedemployee'),
  # department index
  path('departments/', views.departmentIndex, name='departments'),
  # department details
  path('departments/<int:dept_id>/', views.dept_details, name='deptDetails'),
  # add departments
  path('addDept/', views.addDept, name='addDept'),
  #individual employees
  path('employees/<int:id>/', views.employeedetails, name='employeeDetail'),
  path('training/', views.trainingList, name='trainings'),
  path('addTraining/', views.add_training_program, name='add'),
  path('training/<int:id>/', views.trainingDetails, name='trainingDetail'),
  path('editTraining/<int:id>/', views.edit_training_form, name='edit'),
  path('trainingDelete/<int:id>/', views.training_delete, name='trainingDelete')

]
