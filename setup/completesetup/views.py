from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def starts(request):
    return render (request,'Appwork/index.html')

def app(request):
    return render (request,'Apptem/application.html')

