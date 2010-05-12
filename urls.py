# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from feeds import RSSLatestInterviews, AtomLatestInterviews
from sitemap import InterviewsSitemap

feeds = {
    'rss': RSSLatestInterviews,
    'atom': AtomLatestInterviews
    }

urlpatterns = patterns('',                       
                       (r'feed/(?P<url>.*)/?$', 'django.contrib.syndication.views.feed',
                        {'feed_dict': feeds}))

sitemap = {
    'interviews': InterviewsSitemap
    }

urlpatterns += patterns('',
                        (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
                         {'sitemaps': sitemap}))

urlpatterns += patterns('interviews.views',
                       (r'(?P<url>\w+\.\w+)/?$', 'interview'),
                       (r'projekt/?$', 'about'),
                       (r'kontakt/?$', 'contact'),
                       (r'/?$', 'index'),
                       )

