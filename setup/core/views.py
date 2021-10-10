from django.shortcuts import render

from core.models import Student

# Create your views here.

def cores(request):
    return render (request,'./core/about.html')

def cores1(request):
    return render (request,'./core/home.html')

def Models(request):
    stu=Student.objects.all()
    return render(request, 'core/Models.html',{'stud':stu})
