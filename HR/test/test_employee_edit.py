import unittest
from django.test import TestCase
from django.urls import reverse
from HR.models.employeeModels import Employee
from HR.models.departmentModels import Department

class EmployeeEditTest(TestCase):

  def test_employee_edit_geturl(self):

    # create instance of employee to make a valid url arg

    new_dept = Department.objects.create(
      name="Department of Stuff",
      budget="8000"
    )
    new_employee = Employee.objects.create(
      first_name="Django",
      last_name="Reinhardt",
      start_date="2007-12-04",
      is_supervisor= 1,
      department_id= new_dept.id,
    )
    print("EMPLOYEE", new_employee)

    # test whether the get is directing to the correct url
    response = self.client.get(reverse('HR:editemployee', args=(new_employee.id,)))
    print("EDITRESPONSE", response)
    self.assertEqual(response.status_code, 200)

