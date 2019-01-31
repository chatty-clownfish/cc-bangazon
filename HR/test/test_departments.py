import unittest
from django.test import TestCase
from django.urls import reverse

from HR.models.departmentModels import Department

class DepartmentTest(TestCase):

    def test_department_list(self):
      new_dept = Department.objects.create(
        name="Laser Test",
        budget=10,
      )
      response = self.client.get(reverse('HR:departments'))
      self.assertEqual(response.status_code, 200)
      self.assertEqual(len(response.context['department_list']), 1)
      self.assertIn(new_dept.name.encode(), response.content)



    def test_department_details(self):
      new_dept = Department.objects.create(
        name="Laser Test",
        budget=10,
      )
      response = self.client.get(reverse('HR:deptDetails', args=(1, )))
      self.assertEqual(response.context["dept_details"].name, new_dept.name)
      self.assertEqual(response.context["dept_details"].budget, new_dept.budget)

    def test_department_form(self):
      response = self.client.post(reverse('HR:addDept'), {'name':"Department of Testing", 'budget': '200'})
      self.assertEqual(response.status_code, 302)

    
