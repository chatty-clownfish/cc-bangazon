from django.shortcuts import render, get_object_or_404
from HR.models.departmentModels import Department

def departmentIndex(request):
  department_list = Department.objects.all()
  context = { 'department_list' : department_list }
  return render(request, 'HR/department/department.html', context)

def details(request, dept_id):
  dept = get_object_or_404(Department, pk=dept_id)
  context = { 'dept' : dept }
  return render(request, 'HR/department/deptDetails.html', context)