from django.shortcuts import render

# Create your views here.
def employeeList(request, employee_id):
    Employee_list = Employee.objects.filter(employe_id = employee_id)
    print(Employee_list)
    context = {'Employee_list' : Employee_list}
    return render(request, 'HR/views/employeeList.html', context)