from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todo_list, name='show_todo_list'),
    path('json/', show_json, name='json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path("delete-task/<int:id>", delete_task, name="delete_task"),
    path("update-finished/<int:id>", update_finished, name="update_finished"),
    path('add/', add_task_ajax, name = 'add_task_ajax')
]