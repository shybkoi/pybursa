from django.test import TestCase, Client
from courses.models import Course
from students.models import Student
from coaches.models import Coach
from django.contrib.auth.models import User
from datetime import date


class StudentTest(TestCase):

    def test_student_pages(self):
        client = Client()

        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

        coach_tst = Coach.objects.create(name='CoachTest',
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

        student_tst = Student.objects.create(name='Alex',
                                             surname='Testikov',
                                             phone='+380506253635',
                                             email='alextest@bla.com',
                                             date_of_birth=date(1988, 1, 1),
                                             package='Standart',
                                             course=course_tst,)
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testikov")

        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testikov")

    def test_add_student(self):
        client = Client()

        coach_tst = Coach.objects.create(name='CoachTest',
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

        student_tst = Student.objects.create(name='Alex',
                                             surname='Testikov',
                                             phone='+380506253635',
                                             email='alextest@bla.com',
                                             date_of_birth=date(1988, 1, 1),
                                             package='Standart',
                                             course=course_tst,)

        self.assertEqual(Student.objects.all().count(), 1)

    def test_edit_student(self):
        client = Client()

        coach_tst = Coach.objects.create(name='CoachTest',
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

        student_tst = Student.objects.create(name='Alex',
                                             surname='Testikov',
                                             phone='+380506253635',
                                             email='alextest@bla.com',
                                             date_of_birth=date(1988, 1, 1),
                                             package='Standart',
                                             course=course_tst,)

        student_tst = Student.objects.get(id=1)
        student_tst.name = 'Janson'
        student_tst.email='JansonTest@bla.com'
        student_tst.save()

        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Janson")



