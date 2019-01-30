from django.shortcuts import render
from HR.models.employeeModels import Employee
from HR.models.departmentModels import Department


# Create your views here.
def employeeList(request):
    Department_list = Department.objects.all()
    Employee_list = Employee.objects.all()
    print(Employee_list)
    context ={'Employee_list' : Employee_list, 'Department_list': Department_list}
    return render(request, 'HR/employee/employee.html', context)