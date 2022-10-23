from re import template
from django.shortcuts import render,redirect
from task.models import Task
from django.views.generic import View,ListView,DetailView,UpdateView
from task.forms import RegistrationForm,LoginForm,TaskUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.
def required_signin(fn):
    def inner(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"u must login")
            return redirect("sign-in")
        else:
            return fn(request,*args,**kwargs)
    return inner



class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")

class RegView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"reg.html")


@method_decorator(required_signin,name="dispatch")
class AddtaskView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addtask.html")
    def post(self,request,*args,**kwargs):
        # print(request.POST)
        usr=request.user
        task=request.POST.get("Task")
        Task.objects.create(user=usr,task_name=task)
        messages.success(request,"your task has been added sucessfully")
        return redirect("todo-list")

@method_decorator(required_signin,name="dispatch")
class TasklistView(ListView):
    model=Task
    template_name="list-task.html"
    context_object_name="tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # def get(self,request,*args,**kwargs):
    #     if request.user.is_authenticated:
    #           qs=request.user.task_set.all()
    #           return render(request,"list-task.html",{"tasks":qs})
    #     else:
    #         return redirect("sign-in")


@method_decorator(required_signin,name="dispatch")
class TaskDetailView(DetailView):
    model=Task
    template_name="detail.task.html"
    context_object_name="todo"
    pk_url_kwarg="id"
    

    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     task=Task.objects.get(id=id)
    #     return render(request,"detail.task.html",{"todo":task})


@method_decorator(required_signin,name="dispatch")
class TaskDeleteView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        task=Task.objects.get(id=id)
        task.delete()
        messages.success(request,"your task has been deleted")
        return redirect("todo-list")

class TaskUpdateView(UpdateView):
    model=Task
    form_class=TaskUpdateForm
    template_name="update-task.html"
    pk_url_kwarg="id"
    success_url=reverse_lazy("todo-list")


    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     qs=Task.objects.get(id=id)
    #     form=TaskUpdateForm(instance=qs)
    #     return render(request,"todo-update.html",{"form":form})



class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"registration completed sucessfully")
            return redirect("sign-in")
        else:
            messages.error(request,"registration failed")

            return render(request,"registration.html",{"form":form})

class LogView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"log.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login sucesss")

                return redirect("todo-list")
            else:
                messages.error(request,"login  failed")

                return render(request,"log.html",{"form":form})


@required_signin
def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("sign-in")               






