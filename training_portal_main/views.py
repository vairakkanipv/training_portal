from django.shortcuts import render
from django.http import HttpResponse
from academy.models import Course,Trainer,Student
# Create your views here.

def home(request):
    courses = Course.objects.all()
    courses_count = Course.objects.all().count()
    #get trainer counts
    trainers = Trainer.objects.all()
    trainers_count = Trainer.objects.all().count()
    #get student counts
    students = Student.objects.all()
    students_count = Student.objects.all().count

    context = {
        'courses': courses,
        'courses_count' :courses_count,
        'trainers': trainers,
        'trainers_count': trainers_count,
        'students':students,
        'students_count':students_count,
    }
    return render(request,'home.html',context)

def courses(request):
    courses = Course.objects.all()
    courses_count = Course.objects.all().count()

    context ={
        'courses': courses,
        'courses_count': courses_count,
    }
    return render(request,'courses.html',context)

def trainers(request):
    trainers = Trainer.objects.all()
    trainers_count = Trainer.objects.all().count()

    context ={
        'trainers': trainers,
        'trainers_count': trainers_count,
    }
    return render(request,'trainers.html',context)

def students(request):
    students = Student.objects.all()
    students_count = Student.objects.all().count()

    context = {
        'students': students,
        'students_count': students_count,
    }
    return render(request,'students.html',context)