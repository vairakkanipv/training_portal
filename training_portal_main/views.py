from django.shortcuts import render
from django.http import HttpResponse
from academy.models import Course
# Create your views here.

def home(request):
    courses = Course.objects.all()
    courses_count = Course.objects.all().count()
    print(courses_count)
    context = {
        'courses': courses,
        'courses_count' :courses_count
    }
    return render(request,'home.html',context)

def courses(request):
    return render(request,'courses.html')