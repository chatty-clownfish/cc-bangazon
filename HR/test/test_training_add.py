import unittest
from django.test import TestCase
from django.urls import reverse
from HR.models.trainingModels import Training

class TrainingAddTest(TestCase):

    def test_get_training_form(self):
    response = self.client.get(reverse('HR:addtraining'))
    form_test =  '<input type="text" value="{{t.name}}" name="training_name" placeholder="training program name">
        <input type="date" value="{{t.start_date}}" name="training_startDate" placeholder="start date: YYYY-MM-DD">
        <input type="date" value="{{t.end_date}}" name="training_endDate" placeholder="end date: YYYY-MM-DD">
        <input type="text" value="{{t.maxAttendees}}" name="training_maxEnrollment" placeholder="max attendees">
        <input type="submit" value="Save Training">'.encode()
    print('FORMTEST', form_test)
    self.assertIn(form_test, response.content)

