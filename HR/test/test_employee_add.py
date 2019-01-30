import unittest
from django.test import TestCase
from django.urls import reverse
from HR.models.employeeModels import Employee

# Stuff to test
# context: what we send to the template
# content: the rendered html
# response_codes

# Name your tests like this! test_foo so Django can find and run 'em

# * The test client is a Python class that acts as a dummy Web browser, allowing you to test your views and interact with your Django - powered application programmatically. Some of the things you can do with the test client are:
#     * Simulate GET and POST requests on a URL and observe the response – everything from low - level HTTP(result headers and status codes) to page content.
#     * See the chain of redirects(if any) and check the URL and status code at each step.
#     * Test that a given request is rendered by a given Django template, with a template context that contains certain values.

# *  Good rules-of-thumb include having:
#     * a separate TestClass for each model or view
#     * a separate test method for each set of conditions you want to test
#     * test method names that describe their function


class EmployeeAddTest(TestCase):

  def test_get_employee_form(self):
    response = self.client.get(reverse('HR:addemployee'))
    # print('HERE', response.content)
    form_test = '<input type="text" name="first_name">\n  <input type="text" name="last_name">\n  <input type="date" name="start_date">\n  <input type="text" name="is_supervisor">\n  <select name="department_id" id="employee_department">\n    \n  </select>\n  <input type="submit" value="Save Employee">\n</form>\n'.encode()
    # print('THERE', form_test)
    self.assertIn(form_test, response.content)


  def test_post_employee(self):

    response = self.client.post(reverse('HR:addemployee'), {'first_name': 'Randy', 'last_name': 'Savage', 'start_date': "2000-12-14", 'is_supervisor': 1, 'department_id': 2})

    # Getting 302 back because we have a success url and the view is redirecting
    self.assertEqual(response.status_code, 302)


# class ArtistTest(TestCase):

#     def test_get_artist_form(self):

#       response = self.client.get(reverse('history:artist_form'))

#       self.assertIn(
#           '<input type="text" name="name" maxlength="100" required id="id_name">'.encode(), response.content)

    # def test_post_artist(self):

      # response = self.client.post(reverse('history:artist_form'), {'name': 'Bill Board', 'birth_date': '10/31/67', 'biggest_hit': "So Blue Fer You"})

    #   # Getting 302 back because we have a success url and the view is redirecting
    #   self.assertEqual(response.status_code, 302)

#     def test_get_artist_detail(self):
#       new_artist = Artist.objects.create(
#           name="Suzy Saxophone",
#           birth_date="12/25/58",
#           biggest_hit="Honk Honk Squeak"
#       )

#       response = self.client.get(reverse('history:artist_detail', args=(1,)))
#       self.assertEqual(response.context["artist_detail"].name, new_artist.name)