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
2.  Download the following required Python 3.6.x packages (can use `pip install`):
    1.  [django](https://github.com/django/django)
    2.  [requests](https://github.com/requests/requests)
3.  Download [ngrok](https://ngrok.com/download)
4.  Don't download this project folder. We will be building everything from scratch.


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

Next, we have to specify a list of addresses/URLs that may be used to access our server. In the same `newproject/settings.py` file, find `ALLOWED_HOSTS` (right above the previous part), and add in some addresses.
```python
ALLOWED_HOSTS = ['127.0.0.1']
```
This lets our server know that anyone who looks up the address `127.0.0.1` is trying to interact with it.

*Note: `127.0.0.1` is the default 'home' address/url for our machine's local server. We can also change it to the IP address assigned by our router.*


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

Okay, so you've got a cool server. But right now it only exists on your own computer. What good is that?

___

## 2 Exposing to a Local Network

Okay, I heard your concerns. No worries. In this section we'll open up our server to people and machines who are connected on the same network.

We'll start by stopping our server with `Ctrl+C`.

#### 2.1 Finding our Network IP Address

Next, we'll have to figure out our internal IP address.

On terminal, run `ifconfig`.
![task 2.1 screenshot](screenshots/task_2_1.png?raw=true)
Grab the `inet addr` of your machine.

On cmd, run `ipconfig`.
![task 2.1.2 screenshot](screenshots/task_2_1_2.png?raw=true)
Grab the `IPv4 Address` of your machine.

We can see that in **my** own home network, my machine is assigned the address of `172.24.1.134`\* by my router. This will probably change when you're connected to a different network.

\*Note: Placeholder IP address!

#### 2.2 Adding Address to Django

Now, we'll have to tell django to let other network users access our server using `172.24.1.134`\*.

Just like in 1.4, we're gonna add this address into `newproject/settings.py` file, in `ALLOWED_HOSTS`.
```python
ALLOWED_HOSTS = ['127.0.0.1', '172.24.1.134']
```
Save and exit.

\*Placeholder IP address!

#### 2.3 Running Server in Local Network

Now, let's start our server again, with `python manage.py runserver 172.24.1.134:8000`. Notice we specified the address `172.24.1.134`, and port `8000`.

Let's take a look at `172.24.1.134:8000`, shall we?
![task 2.3 screenshot](screenshots/task_2_3.png?raw=true)
Wow, that's really cool!

*What's that? You're not convinced that it actually shows up on other devices in the same network?*

Well, my phone is connected to the same network as my computer right now (see that little wifi thing at the top?). Let's see if it can access the same server.
![task 2.3.2 screenshot](screenshots/task_2_3_2.png?raw=true)
Hey what do you know! Looks like it can. Our work is done.

Stop the server any time with `Ctrl+C`.

___

## Task 3 - Ngrok

Our work is not done.

#### 3.1 Exposing to the WORLD

Now, we have a local server running on port `8000`. We want to open up this port to the world. With that, we use the ngrok tool.

On terminal, run `ngrok http 8000`.

**Windows users**: If you don't have ngrok in your `PATH`, navigate to the folder with the `ngrok.exe` file, and run `ngrok.exe http 8000`.

i.e. `C:\Users\User1\Downloads\ngrok.exe http 8000`

You should be greeted with the following screen
![task 3.1 screenshot](screenshots/task_3_1.png?raw=true)

That thing underlined in red? That's the url to **my** fancy server. But don't go `Ctrl+C/Ctrl+Z`-ing just yet! We can't access it right now. I mean, you can go ahead and do that. But nothing good will come of it.

**Take not of that address. Leave ngrok running.**

*Note: This URL changes every time you start ngrok. They say no two URLs of the same string have been observed in the wild...*

#### 3.2 Configuring Django to use Custom URLs

The smart ones would have realised: we have to once again change up the `newproject/settings.py` file. In `ALLOWED_HOSTS`, add in the custom ngrok address.
```python
ALLOWED_HOSTS = ['127.0.0.1', '172.24.1.134', 'db7a5975.ngrok.io']
```
Save and exit.

#### 3.3 Running the server

Now, let's start our server again, with `python manage.py runserver`. This will leave it running at the default `127.0.0.1:8000`. This is because ngrok will forward the local host address `127.0.0.1` to the world.

Let's take a look at `db7a5975.ngrok.io`, shall we?
![task 3.3 screenshot](screenshots/task_3_3.png?raw=true)
Nice.

*What's that? You're not convinced that it actually shows up on other devices in other networks?*

Well, now my phone is connected to the mobile data network (see that little '4G' thing at the top?). Let's see if it can access the same server.
![task 3.3.2 screenshot](screenshots/task_3_3_2.png?raw=true)
Oh look, it can. What a surprise.

Stop the server any time with `Ctrl+C`.
___

## Task 4 - Interacting with our Server

This is nice and all, but what do I do with this *security risk* of a server that I'd just made?

The answer is, anything you choose, mate!

Let's build a simple, silly adder. For the slower ones out there, an adder is something that adds numbers together. For this we'll just add two numbers.

To interact with the server, we usually send it a `json` package.

*What is a `json`?* It's kinda like a python dictionary, with keys and a value assigned to each key.
In our case, it will look something like this:
```
{
  "number1" : 2,
  "number2" : 5
}
```
Our server will add the values of number1 and number2 together and **hopefully** give us 7.

#### 4.1 Adding Two Numbers

In the `newapp` folder, create a new file called `adder.py`, and fill it with just this:
```python
# in newapp/adder.py
def addNum(package):
    answer = 0
    for num in package:
        answer += package[num]
    return answer
```
This takes a dictionary, sums up all the values associated with each key.

Now, we'll do some modifications to the `newapp/views.py` file. First, we'll import our `adder.py`:
```python
from . import adder
```
Next, we'll edit the `request_msg()` function:

```python
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
```
This just "packages" our `json` into a prettier dictionary, so that our `addNum()` function can easily parse it.

Now, save and exit.

#### 4.2 Put it to the Test!

Go to your browser, and type in `db7a5975.ngrok.io/newapp/`. You should see the following page:
![task 4.2 screenshot](screenshots/task_4_2.png?raw=true)
Well of course! We haven't entered the numbers we want to add.

We wanted to know what is `2 + 5`. Now, at the end of your url, add in `?x=2&y=5`.

i.e. `db7a5975.ngrok.io/newapp/?x=2&y=5`

This is equivalent to sending a package of
```
{
  "x" : 2,
  "y" : 5
}
```
To the server with address `db7a5975.ngrok.io/newapp/`.

Let's have a look at our answer. Hopefully it's 7.
![task 4.2.2 screenshot](screenshots/task_4_2_2.png?raw=true)
Okay, so it says 7.0. But that's just being picky. I think I did pretty good here.

Also, I lied about only adding two numbers. My server can actually add as many numbers as you can throw at it (the smarter ones would have realised it).
![task 4.2.3 screenshot](screenshots/task_4_2_3.jpeg?raw=true)
Cool! Now I can additions stuff pretty much anywhere with an internet connection. Frees up my brain to do other stuff. Like subtractions.


## Further Notes

This is potentially some pretty powerful stuff, what we've built today.

But there are some security concerns with this build. I don't know about you, but I wouldn't trust an unsecured server with my wife.

According to the good folks at [django](https://docs.djangoproject.com/en/dev/ref/django-admin/#django-admin-runserver):
```
DO NOT USE THIS SERVER IN A PRODUCTION SETTING. It has not gone through security audits or performance tests. (And that’s how it’s gonna stay. We’re in the business of making Web frameworks, not Web servers, so improving this server to be able to handle a production environment is outside the scope of Django.)
```
Good luck!

## Acknowledgements

Thanks, django!
Thanks, [NTU Open Source Society](https://github.com/ntuoss)!
Thanks, Linux!
