# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from models import Person


class InterviewsSitemap(Sitemap):

    changefreq = 'never'

    def items(self):
        return Person.objects.all()

    def lastmod(self, obj):
        return obj.date_published

    def location(self, obj):
        return '/'+obj.url+'/'
