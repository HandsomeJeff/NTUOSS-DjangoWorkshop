# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse

from . import adder

# Create your views here.

def request_msg(request):
    if request.method == 'GET':
        data = request.GET
    elif request.method == 'POST':
        data = request.POST
    else:
        return HttpResponse("No Request")
    if data == {}:
        return HttpResponse("Nothing to add here.")
    pack = dict(data)
    package = {}
    statement = ''
    for x in pack:
        try:
            package[str(x)] = float(pack[x][0])
            statement += str(pack[x][0]) + ' + '
        except:
            package[str(x)] = 0
    statement = statement[:-3] + ' = '
    answer = adder.addNum(package)

    return HttpResponse(statement +str(answer))
