# from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is my Home")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')

def service(request):
    return render(request,'service.html')


def why(request):
    return render(request,'why.html')


