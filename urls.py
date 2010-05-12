# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from feeds import RSSLatestInterviews, AtomLatestInterviews


feeds = {
    'rss': RSSLatestInterviews,
    'atom': AtomLatestInterviews
    }

urlpatterns = patterns('',                       
                       (r'feed/(?P<url>.*)/?$', 'django.contrib.syndication.views.feed',
                        {'feed_dict': feeds}))


urlpatterns += patterns('interviews.views',
                       (r'(?P<url>\w+\.\w+)/?$', 'interview'),
                       (r'projekt/?$', 'about'),
                       (r'kontakt/?$', 'contact'),
                       (r'/?$', 'index'),
                       )

