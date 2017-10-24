# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse

# Create your views here.

def request_msg(request):
    return HttpResponse("English can be weird. It can be understood through tough thorough thought, though.")
