from django.shortcuts import render
from .Func.func import Router_Get
# Create your views here.

def Main_Page(request):
    if request.method == "POST":
        pass
    else:
        return Router_Get(request)