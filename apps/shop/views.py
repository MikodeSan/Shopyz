from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Kontan wè zot an lè Freedom-shop :)")
