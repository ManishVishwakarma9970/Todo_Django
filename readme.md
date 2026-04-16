1. Creating Virtual Environment
2. Django install
3. django-admin startproject todo_main .
4. python manage.py migrate
5. python manage.py createsuperuser
----------------
-> (username : djangoadmin)
-> (Email address: manishshethiya13@gmail.com)
-> (Password : manish@9970)

6. creating a views.py and make the home functions.

7. addiing the todo home template in home.html

8. setting the github repository and push the code.

9. creating the app (python manage.py createapp todo) and register the app in settings.py 

10. After that goto models.py and create the class named as "Task" and created the field.

11. after creating the class go to admin.py and register the "task" field and import it.

12. Making the migration "python manage.py makemigrations"

13. Now Migrate it "python manage.py migrate"

14. Creating context in views.py to access the database dynamically on html templates.

15. After Creating this, goto admin.py and configure admin panel like "is_completed", "updated_at" feild to show in the admin database.

16. register in "todo_main" folder in urls.py ---
path('todo/', include(todo.urls)),

17. Adding CRSF token , creating urls.py in "todo" folder.
urlpatterns = [
  path('addTask/', views.add_task, name='addTask'),
]

18. goto views.py and make functions.... add_task().
and making addTask button and input fields functional.

19. in views.py add the line in add_Task functions---
    task = request.POST['task']
    Task.objects.create(task=task)
    <!-- This can List the task on home page and redirect it to home  -->