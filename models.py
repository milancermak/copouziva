# -*- coding: utf-8 -*-
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    occupation = models.CharField(max_length=512)
    date_published = models.DateTimeField()
    image_cropped = models.ImageField()
    image_full = models.ImageField()
    # answers, in HTML
    a1 = models.TextField()
    a2 = models.TextField()
    a3 = models.TextField()
    a4 = models.TextField()
