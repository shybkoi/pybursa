from django.test import TestCase, Client
from courses.models import Course
from coaches.models import Coach
from django.contrib.auth.models import User
from datetime import date


class CourseTest(TestCase):

    def test_course_pages(self):
        client = Client()

        response = client.get('/courses/')
        self.assertEqual(response.status_code, 200)

        coach_tst = Coach.objects.create(name='Test',
                                         surname='Test',
                                         phone='+380506253635',
                                         email='test@bla.com',
                                         position='teacher',
                                         user=User.objects.create(),)

        course_tst = Course.objects.create(technology = 'Python/Django',
                                           name='CourseTest',
                                           description='Test',
                                           start_date=date(2015, 1, 1),
                                           finish_date=date(2015, 1, 30),
                                           teacher=coach_tst,)
        response = client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CourseTest")

        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CourseTest")

    def test_add_course(self):
        client = Client()

        coach_tst = Coach.objects.create(name='Test',
                                         surname='Test',
                                         phone='+380506253635',
                                         email='test@bla.com',
                                         position='teacher',
                                         user=User.objects.create(),)

        course_tst = Course.objects.create(technology = 'Python/Django',
                                           name='CourseTest',
                                           description='Test',
                                           start_date=date(2015, 1, 1),
                                           finish_date=date(2015, 1, 30),
                                           teacher=coach_tst,)

        self.assertEqual(Course.objects.all().count(), 1)

    def test_edit_course(self):
        client = Client()

        coach_tst = Coach.objects.create(name='Test',
                                         surname='Test',
                                         phone='+380506253635',
                                         email='test@bla.com',
                                         position='teacher',
                                         user=User.objects.create(),)

        course_tst = Course.objects.create(technology = 'Python/Django',
                                           name='CourseTest',
                                           description='Test',
                                           start_date=date(2015, 1, 1),
                                           finish_date=date(2015, 1, 30),
                                           teacher=coach_tst,)
        course_tst = Course.objects.get(id=1)
        course_tst.technology = 'Ruby'
        course_tst.name='CourseReTest2'
        course_tst.save()

        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CourseReTest2")



