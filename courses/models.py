from django.db import models
from django.contrib import admin


class Course(models.Model):

    def __unicode__(self):
        return self.technology

    technology = models.CharField(max_length=15,
                                  choices=(('Python','Python/Django'),
                                           ('JS','JavaScript'),
                                           ('Ruby','Ruby on rails')),
                                  default='Python')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    teacher = models.ForeignKey('coaches.Coach', default=1,
                                 related_name='teacher')
    assistant = models.ForeignKey('coaches.Coach', blank=True, null=True,
                                   related_name='assistant')
    start_date = models.DateField()
    finish_date = models.DateField()
    venue = models.ForeignKey('extradata.Address', blank=True, null=True)
