from django.shortcuts import render
from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')  # order_by clause give the data in decendiing order
     # Task model me is_completed naam ka field hai, usme False value wale tasks ko updated_at ke descending order me filter karne ke liye ye karna zaruri hai..
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html', context)
