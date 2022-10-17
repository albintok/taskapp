from django.shortcuts import render,redirect
from task.models import Task
from django.views.generic import View
from task.forms import RegistrationForm,LoginForm
from django.contrib.auth.models import User

# Create your views here.
class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")

class RegView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"reg.html")

class AddtaskView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addtask.html")
    def post(self,request,*args,**kwargs):
        # print(request.POST)
        uname=request.POST.get("Username")
        task=request.POST.get("Task")
        Task.objects.create(user=uname,task_name=task)
        return render(request,"addtask.html")

class TasklistView(View):
    def get(self,request,*args,**kwargs):
        qs=Task.objects.all()
        return render(request,"list-task.html",{"tasks":qs})

class TaskDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        task=Task.objects.get(id=id)
        return render(request,"detail.task.html",{"todo":task})

class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        task=Task.objects.get(id=id)
        task.delete()
        return redirect("todo-list")



class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("todo-list")
        else:
            return render(request,"registration.html",{"form":form})

class LogView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"log.html",{"form":form})





