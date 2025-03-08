from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def just_rooms_by_number(request, rooms):
    return HttpResponse(rooms)
def single_rooms(request):
    return HttpResponse("search single rooms here!")


def double_rooms(request):
    return HttpResponse("search double rooms here")


def just_rooms(request, rooms):
    result = None
    if rooms == 'single rooms':
        result = "check out these single rooms!"
    elif rooms == 'double rooms':
        result = "check out this double rooms!"
    else:
        return HttpResponseNotFound("Type of room not found")
    return HttpResponse(result)
