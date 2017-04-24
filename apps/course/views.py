# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Courses

def index(request):
    context = {
        'courses' : Courses.objects.all()
    }
    return render(request, 'course/index.html', context)

def addnew(request):
    Courses.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def confirm_page(request, id):
    context = {
        'courses' : Courses.objects.all()
    }
    return render(request, 'course/remove.html', context)

def remove(request, id):
    course = Courses.objects.get(id=id)
    course.delete()
    return redirect('/')
