from django.test import TestCase, Client
from coaches.models import Coach
from django.contrib.auth.models import User
from datetime import date


class CoachTest(TestCase):

    def test_coach_pages(self):
        client = Client()

        response = client.get('/coaches/')
        self.assertEqual(response.status_code, 200)

        coach_tst = Coach.objects.create(name='CoachTest',
                                         surname='Test',
                                         phone='+380506253635',
                                         email='test@bla.com',
                                         position='teacher',
                                         user=User.objects.create(),)

        response = client.get('/coaches/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CoachTest")

        response = client.get('/coaches/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CoachTest")

    def test_add_coach(self):
        client = Client()

        coach_tst = Coach.objects.create(name='CoachTest',
                                         surname='Test',
                                         phone='+380506253635',
                                         email='test@bla.com',
                                         position='teacher',
                                         user=User.objects.create(),)

        self.assertEqual(Coach.objects.all().count(), 1)

    def test_edit_coach(self):
        client = Client()

        coach_tst = Coach.objects.create(name='Test',
                                         surname='Test',
                                         phone='+380506253635',
                                         email='test@bla.com',
                                         position='teacher',
                                         user=User.objects.create(),)

        coach_tst = Coach.objects.get(id=1)
        coach_tst.name = 'ReTest'
        coach_tst.email='retest@bla.com'
        coach_tst.save()

        response = client.get('/coaches/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ReTest")



