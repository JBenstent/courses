from django.shortcuts import render, redirect

from .models import *

def index(request):
    courses = Course.objects.all()
    context = {
    'courses': courses
    }
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        content = Course(course_name=request.POST['name'], description=request.POST['description'])
        content.save()
        print content
    return redirect('/')

def delete(request, id):
    course = Course.objects.filter(id=id)
    
    context = {
    'course': course[0]
    }
    return render(request, 'delete.html', context)

def deleteconf(request, id):
    course = Course.objects.filter(id=id)
    course.delete()

    return redirect('/')
