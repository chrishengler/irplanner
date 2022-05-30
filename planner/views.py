from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hey there, this is where the planner will go")
