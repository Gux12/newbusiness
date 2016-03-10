# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from TestModel.models import Musician
from django.core.context_processors import csrf
from django.core import serializers
from forms import UserForm
from django.http import HttpResponseRedirect
import re

# Create your views here.

def index(request):
    # if this is a POST request we need to process the form data
    userlist = Musician.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        Instrument = request.POST['Instrument']
        new_musician = Musician(first_name=FirstName, last_name=LastName, instrument=Instrument)
        new_musician.save()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
    return render(request, 'home.html', {'form': form , 'userlist': userlist})


def delete_musician(request):
    user_id = request.GET['user_id']
    num_id = re.sub(r'\D', "", user_id)
    num_id = int(num_id)
    Musician.objects.filter(id=num_id).delete()
    return render(request, 'home.html')


def checkall(request):
    userlist = Musician.objects.all()
    userlistjson = serializers.serialize("json", userlist)
    print 7
    return HttpResponse(userlistjson)


def check(request):
    keyword = request.GET['keyword']
    print 1
    userlist = Musician.objects.filter(instrument=keyword)
    userlistjson = serializers.serialize("json", userlist)
    return HttpResponse(userlistjson)

