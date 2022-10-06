from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime


todo_list_data = Task.objects.all().values()

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todo_list(request):
    user_data = Task.objects.filter(user=request.user).values()
    context = {
        'todo_list': user_data,  # data untuk HTML
        'nama': request.user.username,
        'user': request.user
    }
    return render(request, 'todolisttest.html', context)

def show_json(request):
    return HttpResponse(serializers.serialize("json", todo_list_data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'registertest.html', context)

def login_user(request):
    context = {
        'todo_list': todo_list_data,  # data untuk HTML
        'nama': request.user.username,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todo_list')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'logintest.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/todolist/login/")
def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
        )
        return HttpResponseRedirect(reverse("todolist:show_todo_list"))
    return render(request, "create_tasktest.html")

@login_required(login_url="/todolist/login/")
def update_finished(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.is_finished = not task.is_finished
    task.save(update_fields=["is_finished"])
    return HttpResponseRedirect(reverse("todolist:show_todo_list"))

@login_required(login_url="/todolist/login/")
def delete_task(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.delete()
    return HttpResponseRedirect(reverse("todolist:show_todo_list"))