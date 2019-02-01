import unittest
from django.test import TestCase
from django.urls import reverse
from HR.models.trainingModels import Training

class TrainingAddTest(TestCase):

    # def test_get_training_form(self):
    # response = self.client.get(reverse('HR:addtraining'))
    # form_test =  '<input type="text" value="{{t.name}}" name="training_name" placeholder="training program name">
    #     <input type="date" value="{{t.start_date}}" name="training_startDate" placeholder="start date: YYYY-MM-DD">
    #     <input type="date" value="{{t.end_date}}" name="training_endDate" placeholder="end date: YYYY-MM-DD">
    #     <input type="text" value="{{t.maxAttendees}}" name="training_maxEnrollment" placeholder="max attendees">
    #     <input type="submit" value="Save Training">'.encode()
    # print('FORMTEST', form_test)
    # self.assertIn(form_test, response.content)

  def test_post_training(self):

    new_training = Training.objects.create(
      name = "John Wood",
      start_date = "2019-09-01",
      end_date = "2019-09-01",
      maxAttendees= "1"    )

    response = self.client.post(reverse('HR:trainings'), {'name': 'John Wood', 'start_date': '2019-09-01', 'end_date': '2019-09-01', 'maxAttendees': 1})
    print("RESPONSE", response.content)
    # Getting 302 back because we have a success url and the view is redirecting
    self.assertEqual(response.status_code, 200)
