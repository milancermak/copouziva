# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from models import Person


def index(request):
    people = Person.objects.filter(published=True)
    return render_to_response('index.html', {'people': people})

def interview(request, url):
    interviewee = get_object_or_404(Person, url=url)
    return render_to_response('interview.html', {'person': interviewee})

def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')
