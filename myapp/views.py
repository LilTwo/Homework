from django.shortcuts import render
from django.http import JsonResponse
from common.decorate import api_json
from .models import Article
from common.orm2json import object_to_json
from django.db import connection
from django.core.cache import cache
from django.shortcuts import render

PAGE_SIZE = 10


def homepage(request):
    return render(request, "homepage.html", {"title": "title1"})


def content(request):
    pass
