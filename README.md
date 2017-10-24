# NTUOSS Django Workshop

*by [Steve](https://github.com/HandsomeJeff) for NTU Open Source Society*

This workshop is based on [nickoala/telepot](https://github.com/nickoala/telepot) and assumes intermediate knowledge of Python.

**Disclaimer:** *This document is only meant to serve as a reference for the attendees of the workshop. It does not cover all the concepts or implementation details discussed during the actual workshop.*
___

### Workshop Details
**When**: Friday, 27 Oct 2017. 6:30 PM - 8:30 PM.</br>
**Where**: Theatre@TheNest, Innovation Centre, Nanyang Technological University</br>
**Who**: NTU Open Source Society

### Questions
Please raise your hand any time during the workshop or email your questions to [me](mailto:yefan0072001@gmail.com) later.

### Errors
For errors, typos or suggestions, please do not hesitate to [post an issue](https://github.com/clarencecastillo/NTUOSS-TelegramBotsWorkshop/issues/new). Pull requests are very welcome! Thanks!
___

## Index

Task 0 - Getting Started
    - 0.1 Introduction
    - 0.2 Initial Setup
___

## Task 0 - Getting Started

#### 0.1 Introduction


For this session, we'll be building a server which allows us to run applications that communicate with the outside world.

This will be hosted entirely on our own machines!

#### 0.2 Initial Setup

1.  Download a text editor of your choice. I strongly recommend either:
    1.  [Atom](https://atom.io/)
    2.  [Sublime Text 3](http://www.sublimetext.com/3)
    3.  [Brackets](http://brackets.io/)
2.  Download [this project]() and unzip the folder to your
<!-- insert project site here -->
3.  Download the following required Python 3.6.x packages (can use `pip install`):
    1.  [django](https://github.com/django/django)
    2.  [requests](https://github.com/requests/requests)
4.  Download [ngrok](https://ngrok.com/download)


## Task 1 - Django

#### 1.1 Create a New Project

On Linux or Mac OS X, open terminal. Navigate to a directory of your choice and enter:
`django-admin newproject`. Leave terminal running.

On Windows, open cmd. Navigate to the directory of your choice and enter:
'"PATH_TO_PYTHON\Scripts\django-admin.exe" startproject newproject'

i.e. If you have Python 3.6 installed, and it is located in your C Drive, then the command will look like:
`"C:\Python36\Scripts\django-admin.py" startproject newproject`. Leave cmd running.

You should see a new folder called *newproject* in the directory.
![task 1.1 screenshot](screenshots/task_1_1.png?raw=true)

#### 1.2 Run the Server

Still on terminal/cmd, enter `cd newproject` to get into the *newproject* folder. Enter `ls` and should see a *new project* folder, and a `manage.py` file.

At this stage, enter `python manage.py runserver` to start the server. This initiates a new server on your machine, with the default address `127.0.0.1`, and port `8000`.
![task 1.2 screenshot](screenshots/task_1_2.png?raw=true)

Now, if you visit `127.0.0.1:8000` on your web browser, you will see the following page:
![task 1.2 screenshot](screenshots/task_1_2_b.png?raw=true)

In the terminal/cmd, use `Ctrl + C` to stop the server.

Congratulations! You now have a working local Django server! Time to add some cool applications, you handsome devil you.

#### 1.3 Create a New App

To create an application, we will execute the following command in the terminal/cmd, in the directory where `manage.py` is:

`python manage.py startapp newapp`

A new folder should appear, with the name *newapp*.
![task 1.3 screenshot](screenshots/task_1_3.png?raw=true)

#### 1.4 Link App to Project
After creating and application, we have to tell Django to use it. We need to edit the file `newproject/settings.py`. Find `INSTALLED_APPS` and add `newproject` just above `]`.
```python
# in newproject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newproject',
]
```
We also have to tell our server to assign a URL to our app. This is so that our app will be accessible to the outside world. For that, we need to edit the file `newproject/urls.py`. Find `urlpatterns` and edit it to this:
```python
# in newproject/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^newapp', include('newapp.urls'))
]
```

Now, whenever our server gets an external request for `127.0.0.1:8000/newapp`, it recognises the `newapp` portion, and forwards the information to our app.

#### 1.5 Configuring the App

Now, we have to create URLs for our app. In the *newapp* folder, create a new file `urls.py`, and enter the following:
```python
# in newapp/urls.py
from django.conf.urls import url
from . import views

app_name = "newapp"

urlpatterns = [
    url(r'^$', views.request_msg, name='request_msg'),
]
```
`views` here contains the 'main logic' of our app. If our app encounters a specific request, it will call a specific function from `views.py`.

The `r'^$'` portion is a `regex` (regular expression) statement. The `^` marks the start, and the `$` marks the end, and everything in between is used as the basis for comparison. In this case, we have nothing in between.

Now, when our server receives a call to `127.0.0.1:8000/newapp`, it calls our app *newapp*, whose `urls.py` then calls `views.py` and executes its `request_msg` function.

*What request_msg function? We don't have a request_msg function in views.py!*

Hey, don't worry about it. Our next step is to edit `views.py`, and change it to the following:
```python
# -*- coding: utf-8 -*-
# in newapp/views.py
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse

# Create your views here.

def request_msg(request):
    return HttpResponse("English can be weird. It can be understood through tough thorough thought, though.")
```

Now, start the server with `python manage.py runserver`.

In your web browser, go to `127.0.0.1:8000/newapp`. You should see the following:
![task 1.5 screenshot](screenshots/task_1_5.png?raw=true)
