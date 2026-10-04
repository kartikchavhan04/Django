from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    return render(request, 'website/index.html')
    # return HttpResponse("Hello, welcome to the home page!")

def about (request):
    return HttpResponse("Hello, welcome to the about page!")

def contact (request):
    return HttpResponse("Hello, welcome to the contact page!")