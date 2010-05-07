# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('interviews.views',
                       (r'(?P<url>\w+\.\w+)/?$', 'interview'),
                       (r'projekt/?$', 'about'),
                       (r'kontakt/?$', 'contact'),
                       (r'/?$', 'index'),
                       )

