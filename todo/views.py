from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.

def add_task(request):
    task = request.POST['task']  # task naam ka input field hai, uska value print karne ke liye ye karna zaruri hai..
    Task.objects.create(task=task)  # Task model me task naam ka field hai, usme task variable ki value store karne ke liye ye karna zaruri hai..
    return redirect('home')  # task add karne ke baad home page par redirect karne ke liye ye karna zaruri hai..