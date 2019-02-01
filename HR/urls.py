from django.urls import path
from . import views


app_name = 'HR'
urlpatterns = [
  # ex: /HR/
  path('', views.index, name='index'),
  # 1. url 2. invoking method 3. nickname for url
  path('addemployee/', views.addEmployee, name='addemployee'),
  # department index
  path('departments/', views.departmentIndex, name='departments'),
  # department details
  path('departments/<int:dept_id>/', views.dept_details, name='deptDetails'),
  # add departments
  path('addDept/', views.addDept, name='addDept'),
  # list of all employees
  path('employees/', views.employeeList , name = 'employees'),
  #individual employees
  path('employees/<int:id>/', views.employeedetails, name='employeeDetail'),
  path('training/', views.trainingList, name='trainings'),
  path('addTraining/', views.add_training_program, name='add'),
  path('training/<int:id>/', views.trainingDetails, name='trainingDetail'),
  path('editTraining/<int:id>/', views.edit_training_form, name='edit'),
  path('trainingDelete/<int:id>/', views.training_delete, name='trainingDelete')

]
