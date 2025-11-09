from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def all_chai(request): 
    return render(request, "chai/all_chai.html")
