from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

from .models import Greeting


def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def debug(request):
    for _ in range(1000):
        greeting = Greeting()
        greeting.save()
    return JsonResponse(settings.DATABASES, json_dumps_params={'indent': 2})


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
