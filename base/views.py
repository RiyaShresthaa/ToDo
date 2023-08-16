from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ToDo

# Create your views here.
def home(request):
    todo_queryset = ToDo.objects.all()
    content = {'todo':todo_queryset}
    return render(request,'home.html',context=content)

def create_todo(request):
    if request.method =="POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')

        ToDo.objects.create(title=title, description=description, status =status)
        return redirect('home')
    return render(request, 'create.html')