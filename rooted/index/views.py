from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect


def index(request):
    template = loader.get_template("index/index.html")
    return HttpResponse(template.render({}, request))
