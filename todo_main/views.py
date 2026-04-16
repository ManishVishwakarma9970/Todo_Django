from django.shortcuts import render
from todo.models import Task


def home(request):
     # Task model me is_completed naam ka field hai, usme False value wale tasks ko updated_at ke descending order me filter karne ke liye ye karna zaruri hai..
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')  # order_by clause give the data in decendiing order

    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')  # order_by clause give the data in decendiing order
    
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        
    }
    return render(request, 'home.html', context)
