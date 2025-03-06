from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def single_rooms(request):
    return HttpResponse("search single rooms here!")


def double_rooms(request):
    return HttpResponse("search double rooms here")
