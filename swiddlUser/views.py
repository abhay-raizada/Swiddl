from django.shortcuts import render

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect, Http404


def index(request):
    context = {}
    return render(request, 'swiddlUser/index.html', context)
# Create your views here.
