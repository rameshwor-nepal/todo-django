from django.shortcuts import render
from django.http import HttpResponse
from .models import Work
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.


def first(request):
    work = Work.objects.all()
    front_end_ma_pathaune_data = {'table_ko_data':work}
    return render(request,'index.html', context=front_end_ma_pathaune_data)


def create(request):
    if request.method=='POST':
        tasks = request.POST.get('task')
        due = request.POST.get('due')
        Work.objects.create(tasks=tasks, due=due)
        return redirect('first')
    return render(request,'index.html')


def detail(request, id):
    work = Work.objects.get(pk=id)
    if request.method == 'POST':
        if request.POST.get('task') and request.POST.get('due'):
                Work.objects.filter(id = id).update(tasks= request.POST.get('task'),due= request.POST.get('due'))
                context={'work': work}
        return redirect('first')
    return render(request, 'detail.html', context={'work':work})


def delete(request, id):
    task_to_delete=Work.objects.get(pk=id)
    task_to_delete.delete()
    return redirect('first')