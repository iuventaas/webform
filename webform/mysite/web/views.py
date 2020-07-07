import os
import subprocess

import redis
from django.shortcuts import render
from .forms import AddForm
from .models import Position


r = redis.Redis(host='rz01')


def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #   form.cleaned_data
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user = request.META.get('REMOTE_ADDR') + " " + request.META.get('HTTP_USER_AGENT')
            r.hset(user, form.cleaned_data['item'], form.cleaned_data['value'])

    # if a GET (or any other method) we'll create a blank form
    else:

        form = AddForm()

    return render(request, 'web/base.html', {'form': form})


def show(request):

    user = request.META.get('REMOTE_ADDR') + " " + request.META.get('HTTP_USER_AGENT')
    elements = r.hgetall(user)
    positions = []
    for key in elements:
        positions.append(Position(key[2:-1], elements[key][2:-1]))

    return render(request, 'web/show.html', {'positions': positions})

