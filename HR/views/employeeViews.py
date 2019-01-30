from django.shortcuts import render, get_object_or_404
from HR.models.departmentModels import Department
from HR.models.employeeModels import Employee
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.




def addEmployee(request):

  if request.method == "GET":
  #render the form page

    department_list = Department.objects.all()
    print(department_list)
    context = {"department_list" : department_list}

    return render(request, 'HR/employee/addemployee.html', context)

  if request.method == "POST":
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    start_date = request.POST["start_date"]
    is_supervisor = request.POST["is_supervisor"]
    department_id = get_object_or_404(Department, pk=request.POST["department_id"])
    # print(first_name)
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
