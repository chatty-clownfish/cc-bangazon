import unittest
from django.test import TestCase
from django.urls import reverse
from HR.models.trainingModels import Training

class TrainingListTest(TestCase):

    def test_list_training(self):
        new_training = Training.objects.create(
            name="Tarkin",
            start_date="2019-2-10",
            end_date="2019-10-10",
            maxAttendees= 21000,
        )


        response = self.client.get(reverse('HR:trainings'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['training_list']), 1)
        print(new_training)
from django.utils import timezone


    # def test_Training(self):
    #     training = Training.objects.create(
    #         name= "deathstar",
    #         start_date = "1992-3-1",
    #         end_date= "1993-3-4",
    #         maxAttendees= 1,
    #     )
    #     # Issue a GET request. "client" is a dummy web browser
    #     # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)

    #     # Check that the rendered context contains 1 artist.
    #     # Response.context is the context variable passed to the template by the view. This is incredibly useful for testing, because it allows us to confirm that our template is getting all the data it needs.
    #     print(new_employee)
    #     print(employeeTraining)
    #     print(training)
    #     self.assertEqual(training.maxAttendies, 1)

    #     # .encode converts from unicode to utf-8
    #     # example:
    #     # If the string is: pythön!
    #     # The encoded version is: b'pyth\xc3\xb6n!'
