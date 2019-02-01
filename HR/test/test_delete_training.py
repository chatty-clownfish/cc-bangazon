import unittest
from django.test import TestCase
from django.urls import reverse
from HR.models.trainingModels import Training
from django.utils import timezone

class TrainingTest(TestCase):

    def test_delete_training(self):
        new_training =  Training.objects.create(

            name = 'im hot for chicken',
            start_date = '2019-4-2',
            end_date = '3000-1-1',
            maxAttendees= 1
        )
        date = timezone.now()
        formatedDate = str(date)[0:10]
        print('formated Date',formatedDate)
        response = self.client.get(reverse('HR:trainingDelete', args =(1, )))
        if new_training.start_date <= formatedDate:
            response.status_code = 400
            print("fail")
            self.assertEqual(response.status_code, 200)
        else:
            print("pass")
            self.assertEqual(response.status_code, 302)
