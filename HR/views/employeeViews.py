from django.shortcuts import render
from HR.models.departmentModels import Department
from HR.models.employeeModels import Employee
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.




def addEmployee(request):

  if request.method == "GET":
  #render the form page
    print("hello")

    department_list = Department.objects.all()
    print(department_list)
    context = {"department_list" : department_list}

    return render(request, 'HR/employee/addemployee.html', context)

  if request.method == "POST":
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    start_date = request.POST["start_date"]
    is_supervisor = request.POST["is_supervisor"]
    department_id = request.POST["department_id"]

    employee_list = Employee.objects.create(first_name=first_name, last_name=last_name, start_date=start_date, is_supervisor=is_supervisor, department_id=department_id)

    context = {"employee_list" : employee_list}

    return render(request, 'HR/employee/employee.html', context)
      # return HttpResponse("Hi")

