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
