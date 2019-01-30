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

class EmployeeListTest(TestCase):

    def test_list_employee(self):
        new_employee = Employee.objects.create(
            first_name="Suzy",
            last_name="Saxophone",
            start_date="1992-10-10",
            is_supervisor= 1,
            department_id= 2,
        )

        # Issue a GET request. "client" is a dummy web browser
        # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get(reverse('HR:employees'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 1 artist.
        # Response.context is the context variable passed to the template by the view. This is incredibly useful for testing, because it allows us to confirm that our template is getting all the data it needs.
        self.assertEqual(len(response.context['Employee_list']), 1)
        print(new_employee)
        # .encode converts from unicode to utf-8
        # example:
        # If the string is: pythön!
        # The encoded version is: b'pyth\xc3\xb6n!'