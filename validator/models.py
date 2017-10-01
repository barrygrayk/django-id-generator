# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
# from django_countries.fields import CountryField
from django.db import models
from .idgenerator import unique_slug_generator

# Create your models here.


genders = (
    ('male','Male'),
    ('female', 'Female'),
)
races = (
    ('black','Black'),
    ('white', 'White'),
    ('other', 'Other'),
)
class Person (models.Model):

    name = models.CharField(max_length=120)
    date_of_birth =  models.DateField(auto_now_add=False,default='%m/%d/%y')
    gender = models.CharField(max_length=6,choices=genders,default='female')
    country = models.CharField(max_length=120)
    # country = CountryField()
    race = models.CharField(max_length=8,choices=races,default='white')
    sa_id = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('validator:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

def rl_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.sa_id:
        instance.sa_id = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver,sender=Person)