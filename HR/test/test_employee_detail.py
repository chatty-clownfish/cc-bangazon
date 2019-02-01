import unittest
from django.test import TestCase
from django.urls import reverse
from HR.models.employeeModels import Employee


class EmployeeDetailListTest(TestCase):

    def test_list_employeeDetail(self):
        new_employee = Employee.objects.create(
            first_name="Suzy",
            last_name="Saxophone",
            start_date="1992-10-10",
            is_supervisor= 1,
            department_id= 2,
        )

        response = self.client.get(reverse('HR:employeeDetail', args= (1, )))
        self.assertEqual(response.context['employee'].first_name, new_employee.first_name)

