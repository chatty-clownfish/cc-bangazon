from django.shortcuts import render
from HR.models.departmentModels import Department
from HR.models.employeeModels import Employee
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.




def addEmployee(request):

  if request.method == "GET":
  #render the form page
    return render(request, 'HR/employee/addEmployee.html')

  if request.method == "POST":
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    start_date = request.POST["start_date"]
    is_supervisor = request.POST["is_supervisor"]
    department = request.POST["department"]

    employee_list = Employee.objects.create(first_name=first_name, last_name=last_name, start_date=start_date, is_supervisor=is_supervisor)
    
    department_list = Department.objects.all()
    context = {"department_list" : department_list, "employee_list" : employee_list}

    return render(request, 'HR/employee/addEmployee.html', context)
      # return HttpResponse("Hi")

