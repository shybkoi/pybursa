from django.db import models


class Student(models.Model):

    def __unicode__(self):
        return self.surname

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=15,
                               choices=(('Standart','Standart'),
                                        ('Gold','Gold')),
                               default='Standart')
    course = models.ForeignKey('courses.Course', default=1)
    dossier = models.OneToOneField('extradata.Dossier', blank=True, null=True)
