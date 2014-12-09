from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):

    def __unicode__(self):
        return self.surname

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=15,
                                  choices=(('teacher','teacher'),
                                           ('assistant','assistant')),
                                  default='teacher')
    user = models.ForeignKey(User, default=1)
    dossier = models.OneToOneField('extradata.Dossier', blank=True, null=True)
