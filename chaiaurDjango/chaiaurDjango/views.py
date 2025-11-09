from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hi i am shbham kumar and you are at django home page")
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")
    
    