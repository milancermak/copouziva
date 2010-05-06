# -*- coding: utf-8 -*-
from django.db import models

# not the smartes way to do it, but it's easy to understand
# and it was developed fast - works for me
class Person(models.Model):
    name = models.CharField(max_length=256) # name + surname
    url = models.CharField(max_length=256) # string "name.surname" without national chars
    occupation = models.CharField(max_length=512)
    date_published = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)
    image_thumb = models.ImageField(upload_to='images/thumbnails', help_text="500x100 px")
    image_full = models.ImageField(upload_to='images/portraits', help_text="500x335 px")
    # HTML formatted answers
    a1 = models.TextField()
    a2 = models.TextField()
    a3 = models.TextField()
    a4 = models.TextField()

    class Meta:
        ordering = ['-date_published']

    def __unicode__(self):
        return self.name
    
