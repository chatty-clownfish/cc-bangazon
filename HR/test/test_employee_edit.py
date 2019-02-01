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


  def test_get_employee_edit_form(self):

    # create instance of employee

    dept_of_stuff = Department.objects.create(
      name="Department of Stuff",
      budget="8000"
    )
    new_employee = Employee.objects.create(
      first_name="Emmet",
      last_name="Ray",
      start_date="2008-05-03",
      is_supervisor= 0,
      department_id= dept_of_stuff.id,
    )
    print("EMPLOYEE", new_employee)

    # test whether the get is retrieving template with employee info as existing value

    response = self.client.get(reverse('HR:editemployee', args=(new_employee.id,)))
    form_return = 'First Name: <input type="text" name="first_name" value="Emmet"><br />\n  Last Name: <input type="text" name="last_name" value="Ray"><br />\n  Start date: <input type="date" name="start_date" value="2008-05-03"><br />\n  Supervisor Status:\n  <input type="radio" name="is_supervisor" value=1>Yes\n  <input type="radio" name="is_supervisor" checked="checked" value=0>No<br />\n  Department: <select name="department_id" id="employee_department">\n    \n    <option value="1">Department of Stuff</option>\n    \n  </select><br /><br />\n  <input type="submit" value="Save Employee">\n</form>\n'.encode()
    print('FORMRETURN', form_return)
    self.assertIn(form_return, response.content)

    # test that edited info is posting from the form back to the employee detail

  def test_post_edit_employee(self):

    # create instance of employee

    dept_of_things = Department.objects.create(
      name="Department of Things",
      budget="10000"
    )
    new_employee = Employee.objects.create(
      first_name="Bruce",
      last_name="Willis",
      start_date="2010-05-05",
      is_supervisor= 1,
      department_id= dept_of_things.id,
    )
    print("EMPLOYEE", new_employee)

  