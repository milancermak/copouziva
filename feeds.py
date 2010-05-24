# -*- coding: utf-8 -*-

from django.contrib.syndication import feeds
from django.utils.feedgenerator import Atom1Feed
from models import Person


class RSSLatestInterviews(feeds.Feed):

    link = '/'
    title = 'Čo používa'
    description = 'Nové rozhovory na Čo používa.'

    def items(self):
        return Person.objects.filter(published=True)[:7] # last seven

    def item_link(self, item):
        return '/'+item.url+'/'

class AtomLatestInterviews(RSSLatestInterviews):

    feed_type = Atom1Feed
    subtitle = RSSLatestInterviews.description
