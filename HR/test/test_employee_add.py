import unittest
from django.test import TestCase
from django.urls import reverse
from HR.models.employeeModels import Employee
from HR.models.departmentModels import Department

class EmployeeAddTest(TestCase):

  def test_get_employee_form(self):
    response = self.client.get(reverse('HR:addemployee'))
    form_test = 'First Name: <input type="text" name="first_name" placeholder="First name"><br />\n  Last Name: <input type="text" name="last_name" placeholder="Last name"><br />\n  Start date: <input type="date" name="start_date"><br />\n  Supervisor Status:<br />\n  <input type="checkbox" name="is_supervisor" value=True>Yes<br>\n  <input type="checkbox" name="is_supervisor" value=False>No<br>\n  Department: <select name="department_id" id="employee_department">\n    \n  </select><br /><br />\n  <input type="submit" value="Save Employee">\n</form>\n'.encode()
    print('FORMTEST', form_test)
    self.assertIn(form_test, response.content)
    

  def test_post_employee(self):

    new_dept = Department.objects.create(
      name="Department of Stuff",
      budget="8000"
    )

    response = self.client.post(reverse('HR:addemployee'), {'first_name': 'Randy', 'last_name': 'Savage', 'start_date': '2000-12-14', 'is_supervisor': 1, "department_id": new_dept.id})
    print("RESPONSE", response.content)
    # Getting 302 back because we have a success url and the view is redirecting
    self.assertEqual(response.status_code, 302)