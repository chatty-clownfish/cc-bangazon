from django.shortcuts import render, get_object_or_404
from HR.models.departmentModels import Department
from HR.models.employeeModels import Employee
from HR.models.employeeTrainingModels import EmployeeTraining
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def addEmployee(request):

  # if you're not currently on the add employee page
  if request.method == "GET":
    # get the departments so that names can display in the dropdown menu
    department_list = Department.objects.all()
    context = {"department_list" : department_list}
    #render the form page
    return render(request, 'HR/employee/addemployee.html', context)

  # if you're on the add employee page
  if request.method == "POST":
    print("add employee post called")
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    start_date = request.POST["start_date"]
    is_supervisor = request.POST["is_supervisor"]
    department_id = get_object_or_404(Department, pk=request.POST["department_id"])
    # create the employee object and save to database
    employee_list = Employee.objects.create(first_name=first_name, last_name=last_name, start_date=start_date, is_supervisor=is_supervisor, department_id=department_id.id)
    # reverse statement is telling urls.py which address to go to and which method to invoke
    return HttpResponseRedirect(reverse('HR:employees'))

# Create your views here.
def employeeList(request):
    Department_list = Department.objects.all()
    Employee_list = Employee.objects.all()
    print(Employee_list)
    context ={'Employee_list' : Employee_list, 'Department_list': Department_list}
    return render(request, 'HR/employee/employee.html', context)

def employeedetails(request, id):
    employee = get_object_or_404(Employee, pk= id)
    employeetraining = EmployeeTraining.objects.filter(employee_id= id)
    context = { 'employee' : employee, 'employeetraining' : employeetraining }
    print(context)
    return render(request, 'HR/employee/employeeDetail.html', context)


