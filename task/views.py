from django.shortcuts import render
from task.models import Task
from django.views.generic import View

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
    
    




