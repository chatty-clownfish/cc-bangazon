from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


from HR.models.departmentModels import Department
from HR.models.employeeModels import Employee

def departmentIndex(request):
  department_list = Department.objects.all()
  context = { 'department_list' : department_list }
  return render(request, 'HR/department/department.html', context)

def dept_details(request, dept_id):
  dept_details = get_object_or_404(Department, pk=dept_id)
  employees = Employee.objects.filter(department_id=dept_id)
  context = { 'dept_details' : dept_details, 'employees' : employees }
  return render(request, 'HR/department/deptDetails.html', context)

def addDept(request):
    name = request.POST['name']
    budget = request.POST['budget']
    department = Department(name=name, budget=budget)
    department.save()
    return HttpResponseRedirect(reverse('HR:departments'))