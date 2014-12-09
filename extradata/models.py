from django.db import models


class Address(models.Model):

    def __unicode__(self):
        return str(self.city) + ', ' + str(self.street) + ', ' \
        + str(self.building)

    zip_code = models.CharField(max_length=15, default='')
    country = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    street = models.CharField(max_length=255, default='')
    building = models.CharField(max_length=5, default='')


class Dossier(models.Model):

    def __unicode__(self):
        return str(self.adress) + ' - ' + str(self.favorite_color)

    adress = models.ForeignKey(Address, blank=True, null=True)
    unliked_courses = models.ManyToManyField('courses.Course')
    favorite_color = models.CharField(max_length=15,
                                  choices=(('red','red'),
                                           ('orange','orange'),
                                           ('yellow','yellow'),
                                           ('green','green'),
                                           ('blue','blue'),
                                           ('indigo','indigo'),
                                           ('purple','purple')),
                                  default='red')

