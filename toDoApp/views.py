from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import toDOItem

def toDoView(request):
    all_todo_items = toDOItem.objects.all()
    return render(request,'index.html',{'all_items':all_todo_items})

def addItem(request):
    toDOItem(item = request.POST['item']).save()
    return HttpResponseRedirect('/toDoApp/')

def deleteItem(request, todo_id):
    toDOItem.objects.get(id = todo_id).delete()
    return HttpResponseRedirect('/toDoApp/')