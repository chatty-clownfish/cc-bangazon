from django.shortcuts import render, get_object_or_404
from HR.models.departmentModels import Department

def departmentIndex(request):
  department_list = Department.objects.all()
  context = { 'department_list' : department_list }
  return render(request, 'HR/department/department.html', context)