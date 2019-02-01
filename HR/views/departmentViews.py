from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# import all the modles django needs

# import Classes needed by views
from HR.models.departmentModels import Department
from HR.models.employeeModels import Employee

# Department.objects.all pull all of the departments from the database, context stores them in a dictionary and the return statement will use the template to form the page with the data
def departmentIndex(request):
  department_list = Department.objects.all()
  context = { 'department_list' : department_list }
  return render(request, 'HR/department/department.html', context)

# Get the specific details of the chosen department, dept_details fetches the information of a specific department, employees fetches the employees that have that department id so that you can see who works in what department, context stores the information in a dictionary.  The data is returned through the template to display the page
def dept_details(request, dept_id):
  dept_details = get_object_or_404(Department, pk=dept_id)
  employees = Employee.objects.filter(department_id=dept_id)
  context = { 'dept_details' : dept_details, 'employees' : employees }
  return render(request, 'HR/department/deptDetails.html', context)

# Add a department to the list.  The POST method consturcts a new department and saves the inforamtion passed into it by the user
def addDept(request):
  if request.method == "POST":
    name = request.POST['name']
    budget= request.POST['budget']
    d = Department(name = name, budget = budget)
    d.save()
    response = redirect('HR:departments')
    return response
  if request.method == "GET":
    return render(request, 'HR/department/addDept.html')