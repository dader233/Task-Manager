from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required  
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user = request.user)
    return render(request, 'tasks/task_list.html', {'tasks' : tasks})

@login_required
def task_create(request):
    if request.method ==  'POST':
        Task.objects.create(
            title = request.POST['title'],
            description = request.POST.get('description', ''),
            user = request.user,
            status = request.POST['status'],
            priority = request.POST['priority']
        )
        messages.success(request, 'Таска создана')
    return redirect('task_list')

@login_required
def task_update(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.status = request.POST['status']
        task.priority = request.POST['priority']
        task.save()
        messages.success(request, 'Задача обновлена!')
        return redirect('task_list')
    return render(request, 'tasks/task_edit.html', {'task': task})

@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Задача удалена!')
        return redirect('task_list')
    return render(request, 'tasks/task_list.html', {'tasks': Task.objects.filter(user=request.user)})

@login_required
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})
