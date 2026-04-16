from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.

def add_task(request):
    task = request.POST['task']  # task naam ka input field hai, uska value print karne ke liye ye karna zaruri hai..
    Task.objects.create(task=task)  # Task model me task naam ka field hai, usme task variable ki value store karne ke liye ye karna zaruri hai..

    return redirect('home')  # task add karne ke baad home page par redirect karne ke liye ye karna zaruri hai..



def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Task model me se pk ke basis par task ko get karne ke liye ye karna zaruri hai..
    task.is_completed = True  # task ko complete mark karne ke liye is_completed field ko True set karna zaruri hai..
    task.save()
    return redirect('home')  # task complete karne ke baad home page par redirect karne ke liye ye karna zaruri hai..


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Task model me se pk ke basis par task ko get karne ke liye ye karna zaruri hai..
    task.is_completed = False  # task ko incomplete mark karne ke liye is_completed field ko False set karna zaruri hai..
    task.save()
    return redirect('home')  # task incomplete karne ke baad home page par redirect karne ke liye ye karna zaruri hai..



def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)  # Task model me se pk ke basis par task ko get karne ke liye ye karna zaruri hai..
    if request.method == 'POST':
        new_task = request.POST['task']  # task naam ka input field hai, uska value print karne ke liye ye karna zaruri hai..
        get_task.task = new_task  # get_task variable me jo task object store hai,
        get_task.save()  # task ko update karne ke baad save karna zaruri hai..
        return redirect('home')  # task update karne ke baad home page par redirect

    else :
        context = {
            'get_task': get_task,
        }
    
        return render(request, 'edit_task.html', context)


    
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Task model me se pk ke basis par task ko get karne ke liye ye karna zaruri hai..
    task.delete()  # task ko delete karne ke liye ye karna zaruri hai..
    return redirect('home')  # task delete karne ke baad home page par redirect karne ke liye ye karna zaruri hai..