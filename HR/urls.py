from django.urls import path
from . import views


app_name = 'HR'
urlpatterns = [
  # ex: /HR/
  path('', views.index, name='index'),
<<<<<<< Updated upstream
=======


  # department index
  path('departments/', views.departmentIndex, name='departments'),
  # department details
  path('departments/<int:dept_id>/', views.details, name='deptDetails'),

>>>>>>> Stashed changes
  path('employees/', views.employeeList , name = 'employees'),
]

