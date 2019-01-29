from django.shortcuts import render, get_object_or_404

from HR.models import Department

def departmentIndex(request):
  department_list = Department.objects.all()
  context = { 'department_list' : department_list }
  return render(request, 'HR/department/departmentView.html', context)